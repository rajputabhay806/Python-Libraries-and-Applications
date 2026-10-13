import numpy as np
arr = np.arange(1, 16)
arr[arr % 3 == 0] = -1
print(arr)
