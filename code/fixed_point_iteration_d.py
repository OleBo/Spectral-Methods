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

# Accurate fixed point (from many iterations)
x_star = 0.7390851332151606  # high-precision value




def newton_cos(x0, n_iter=10):
    x = x0
    history = [x]
    for i in range(n_iter):
        x = x + (np.cos(x) - x) / (np.sin(x) + 1)
        history.append(x)
    return history

x0 = 0.5
fp_iter = fixed_point_iteration(x0, n_iter=10)
newton_iter = newton_cos(x0, n_iter=5)  # Newton converges faster

# Compute errors
fp_errors = [abs(x - x_star) for x in fp_iter[:-1]]
newton_errors = [abs(x - x_star) for x in newton_iter[:-1]]

plt.figure(figsize=(8,5))
plt.semilogy(fp_errors, 'o-', label='Fixed point iteration')
plt.semilogy(newton_errors, 's-', label="Newton's method")
plt.xlabel('Iteration n')
plt.ylabel('Error')
plt.title('Convergence Comparison')
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.legend()
plt.savefig('fixed_point_iteration_d.png', dpi=150, bbox_inches='tight')
plt.show(block=False)
plt.pause(0.001)

print("Newton iterates:")
for i, val in enumerate(newton_iter):
    print(f"x_{i} = {val:.10f}")
