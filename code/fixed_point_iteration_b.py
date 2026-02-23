import numpy as np
import matplotlib.pyplot as plt

def fixed_point_iteration(x0, n_iter=20):
    x = x0
    history = [x]
    for i in range(n_iter):
        x = np.cos(x)
        history.append(x)
    return history

x0 = 0.5
iterates = fixed_point_iteration(x0)
print("Iterates:")
for i, val in enumerate(iterates):
    print(f"x_{i} = {val:.10f}")
