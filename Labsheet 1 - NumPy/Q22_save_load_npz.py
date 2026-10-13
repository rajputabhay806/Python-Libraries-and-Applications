import numpy as np
a = np.arange(5)
b = np.arange(12).reshape(3, 4)
c = np.array([2.5, 3.5])
np.savez("arrays.npz", numbers=a, matrix=b, decimals=c)
with np.load("arrays.npz") as data:
    print("Stored array names:", data.files)
