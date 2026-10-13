import numpy as np
arr = np.arange(1, 37).reshape(6, 6)
corners = np.array([arr[0, 0], arr[0, -1], arr[-1, 0], arr[-1, -1]])
print(arr)
print("Corners [top-left, top-right, bottom-left, bottom-right]:", corners)
