import numpy as np
from Pyfhel import Pyfhel

print("1. Imported Pyfhel class")

HE = Pyfhel()
HE.contextGen(scheme='bfv', n=2**14, t_bits=20)
HE.keyGen()
print("2. Context and key setup\n", HE)

integer1 = np.array([127], dtype=np.int64)
integer2 = np.array([-2], dtype=np.int64)

cypherText1 = HE.encryptInt(integer1)
cypherText2 = HE.encryptInt(integer2)

print("3. Integer encryption\n", "int", integer1, " -> ctext", type(cypherText1), "\nint", integer2, "-> ctext2", type(cypherText2))

cypherTextSum = cypherText1 + cypherText2
cypherTextSub = cypherText1 - cypherText2
cypherTextMul = cypherText1 * cypherText2

resSum = HE.decryptInt(cypherTextSum)
resSub = HE.decryptInt(cypherTextSub)
resMul = HE.decryptInt(cypherTextMul)

print("4. Decrpyted results:\n  addition =", resSum, "\n    subtraction =", resSub, "\n multiplication =", resMul)