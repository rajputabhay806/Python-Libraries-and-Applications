import numpy as np
marks = np.array([[80, 75, 90, 85], [70, 88, 76, 80], [92, 91, 89, 95],
                  [65, 72, 68, 70], [85, 87, 84, 90]])
print("Each student's average:", marks.mean(axis=1))
print("Each subject's average:", marks.mean(axis=0))
