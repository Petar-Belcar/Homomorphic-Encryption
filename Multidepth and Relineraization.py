import numpy as np
from Pyfhel import Pyfhel, PyCtxt, PyPtxt

n_mults = 10
HE_client = Pyfhel(key_gen=True, context_params ={
    'scheme': 'CKKS',
    'n': 2**14,
    'scale': 2**30,
    'qi_sizes': [30] * (n_mults + 4)
})

HE_client.keyGen()             
HE_client.relinKeyGen()
HE_client.rotateKeyGen()

x = np.array([1000])
cx = HE_client.encrypt(x)

s_context    = HE_client.to_bytes_context()
s_public_key = HE_client.to_bytes_public_key()
s_relin_key  = HE_client.to_bytes_relin_key()
s_rotate_key = HE_client.to_bytes_rotate_key()
s_cx         = cx.to_bytes()

HE_server = Pyfhel()
HE_server.from_bytes_context(s_context)
HE_server.from_bytes_public_key(s_public_key)
HE_server.from_bytes_relin_key(s_relin_key)
HE_server.from_bytes_rotate_key(s_rotate_key)
cx = PyCtxt(pyfhel=HE_server, bytestring=s_cx)
print(f"[Server] received HE_server={HE_server} and cx={cx}")

nova_placa = cx + HE_server.encode(np.array([200]))
nova_placa *= HE_server.encode(np.array([1.2]))

res = HE_client.decryptFrac(nova_placa)[0]

print(f"[Client] Response received! Result is {np.round(res, 4)}, should be {1200 * 1.2}")