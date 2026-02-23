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

# Accurate fixed point (from many iterations)
x_star = 0.7390851332151606  # high-precision value

errors = [abs(x - x_star) for x in iterates[:-1]]  # errors at each step before update
plt.figure(figsize=(8,5))
plt.semilogy(errors, 'o-', label='|x_n - x*|')
plt.xlabel('Iteration n')
plt.ylabel('Error')
plt.title('Convergence of Fixed Point Iteration for x = cos(x)')
plt.grid(True, which='both', linestyle='--', alpha=0.7)

# Add theoretical slope line
L = np.sin(1)
plt.semilogy([0, len(errors)-1], [errors[0], errors[0]*L**(len(errors)-1)], 
             'r--', label=f'Theoretical slope L={L:.3f}')
plt.legend()
plt.savefig('fixed_point_iteration_c.png', dpi=150, bbox_inches='tight')
plt.show(block=False)
plt.pause(0.001)

# Compute empirical convergence factor
ratios = [errors[i+1]/errors[i] for i in range(len(errors)-1)]
print("Error reduction ratios:")
for i, r in enumerate(ratios):
    print(f"e_{i+1}/e_{i} = {r:.5f}")
print(f"Average ratio: {np.mean(ratios):.5f}")
print(f"Theoretical L: {L:.5f}")
