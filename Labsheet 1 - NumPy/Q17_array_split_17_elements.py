import numpy as np
arr = np.arange(17)
parts = np.array_split(arr, 4)
for i, part in enumerate(parts, start=1):
    print(f"Part {i}: {part}; size={part.size}")
