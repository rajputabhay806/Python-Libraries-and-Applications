import numpy as np
arr = np.arange(1, 11, dtype=int)
float_arr = arr.astype(float)
print("Original:", arr, arr.dtype)
print("Converted:", float_arr, float_arr.dtype)
