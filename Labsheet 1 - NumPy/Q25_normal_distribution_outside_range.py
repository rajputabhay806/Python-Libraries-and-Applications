import numpy as np
rng = np.random.default_rng()
sample = rng.normal(loc=0, scale=2, size=2000)
outside = np.abs(sample) > 4
print("Count outside [-4, 4]:", int(outside.sum()))
