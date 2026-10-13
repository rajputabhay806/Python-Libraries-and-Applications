import numpy as np
arr = np.random.default_rng().integers(0, 100, size=(5, 5))
np.savetxt("random_array.csv", arr, delimiter=",", fmt="%d")
loaded = np.loadtxt("random_array.csv", delimiter=",", dtype=int)
print("Original:\n", arr)
print("Loaded:\n", loaded)
print("Arrays match:", np.array_equal(arr, loaded))
