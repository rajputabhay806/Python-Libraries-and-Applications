import numpy as np
a = np.array([1, 2, 3])
b = np.array([[4, 5]])
c = np.array([6, 7])
combined = np.concatenate((a.reshape(-1), b.reshape(-1), c.reshape(-1)))
print(combined)
