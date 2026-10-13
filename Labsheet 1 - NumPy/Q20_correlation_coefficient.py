import numpy as np
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 6])
print("Correlation matrix:\n", np.corrcoef(x, y))
print("Correlation coefficient:", np.corrcoef(x, y)[0, 1])
