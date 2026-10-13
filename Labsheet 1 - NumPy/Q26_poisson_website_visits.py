import numpy as np
rng = np.random.default_rng()
visits = rng.poisson(lam=5, size=60)
minute = int(np.argmax(visits)) + 1
print("Visits per minute:", visits)
print(f"Highest visits: {visits[minute - 1]} at minute {minute}")
