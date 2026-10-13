import numpy as np
arr = np.arange(32).reshape(2, 4, 4)
part1, part2 = np.split(arr, 2, axis=0)
print("Part 1 shape:", part1.shape, "\n", part1)
print("Part 2 shape:", part2.shape, "\n", part2)
