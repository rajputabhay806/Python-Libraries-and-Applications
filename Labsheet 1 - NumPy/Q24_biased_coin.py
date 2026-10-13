import numpy as np
rng = np.random.default_rng()
flips = rng.binomial(n=1, p=0.7, size=200)  # 1 = heads, 0 = tails
heads = int(flips.sum())
print("Heads:", heads)
print("Observed proportion of heads:", heads / len(flips))
