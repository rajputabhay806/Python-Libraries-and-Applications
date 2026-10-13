import numpy as np
a = np.arange(1, 7).reshape(2, 3)
b = np.arange(7, 13).reshape(2, 3)
stacked = np.stack((a, b))
print(stacked)
print("Shape:", stacked.shape)
