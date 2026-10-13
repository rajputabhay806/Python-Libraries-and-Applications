import numpy as np
rng = np.random.default_rng()
counts = rng.multinomial(n=200, pvals=[0.5, 0.3, 0.2])
for product, count in zip(["Product A", "Product B", "Product C"], counts):
    print(f"{product}: {count}")
