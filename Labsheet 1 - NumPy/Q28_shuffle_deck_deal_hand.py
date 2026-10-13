import numpy as np
rng = np.random.default_rng()
deck = rng.permutation(np.arange(1, 53))
hand = deck[:5]
print("Shuffled deck:", deck)
print("5-card hand:", hand)
