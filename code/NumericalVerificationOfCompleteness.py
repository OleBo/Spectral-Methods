import math
import matplotlib.pyplot as plt
import numpy as np
from decimal import Decimal, getcontext

# Set high precision for calculations
getcontext().prec = 50

def babylonian_sqrt_2(n_terms=10):
    """Generate Babylonian sequence for sqrt(2) as rational approximations."""
    # Start with rational approximation: 1 = 1/1
    sequence = [Decimal(1)]
    
    for i in range(1, n_terms):
        x_n = sequence[-1]
        x_next = (x_n + Decimal(2)/x_n) / Decimal(2)
        sequence.append(x_next)
    
    return sequence

def analyze_sequence(seq):
    """Analyze properties of the sequence."""
    print("="*60)
    print("ANALYSIS OF CAUCHY SEQUENCE CONVERGING TO √2")
    print("="*60)
    
    print(f"\nGenerated {len(seq)} terms:")
    for i, term in enumerate(seq[:10]):  # Show first 10 terms
        print(f"  x_{i} = {term:.15f}")
    if len(seq) > 10:
        print(f"  ... and {len(seq)-10} more terms")
    
    # 1. Show it's a Cauchy sequence
    print("\n" + "-"*40)
    print("1. VERIFYING CAUCHY PROPERTY")
    print("-"*40)
    
    # Compute maximum differences for tail
    n = len(seq)
    cauchy_epsilons = []
    for N in [1, 2, 3, 5, 8]:
        if N < n:
            max_diff = max(abs(seq[i] - seq[j]) 
                          for i in range(N, n) 
                          for j in range(N, n) 
                          if i < j)
            cauchy_epsilons.append((N, float(max_diff)))
            print(f"  For N={N}: max|xi - xj| < {max_diff:.10f}")
    
    # 2. Show it doesn't converge in Q
    print("\n" + "-"*40)
    print("2. NON-CONVERGENCE IN ℚ")
    print("-"*40)
    
    sqrt2 = Decimal(2).sqrt()
    differences = [abs(term - sqrt2) for term in seq]
    
    print(f"  Actual limit: √2 = {sqrt2:.15f}")
    print(f"  Last term: x_{n-1} = {seq[-1]:.15f}")
    print(f"  Difference: |x_n - √2| = {differences[-1]:.15e}")
    
    # Check if any term equals √2 exactly (it won't in Q)
    exact_match = any(term == sqrt2 for term in seq)
    print(f"  Exact match with √2 in sequence? {exact_match}")
    print(f"  √2 is irrational, so cannot be represented exactly in ℚ")
    
    # 3. Show convergence in ℝ (completion of ℚ)
    print("\n" + "-"*40)
    print("3. COMPLETION: ADDING √2 TO ℚ")
    print("-"*40)
    
    print("  Let ℝ = ℚ ∪ {irrationals like √2, π, e, ...}")
    print(f"  In ℝ, our sequence converges: lim x_n = {sqrt2:.15f}")
    print(f"  Error at last term: {differences[-1]:.2e}")
    
    # 4. Verify convergence rate
    print("\n" + "-"*40)
    print("4. CONVERGENCE RATE ANALYSIS")
    print("-"*40)
    
    # Compute ratios of successive errors
    print("  n    x_n                |x_n - √2|     Ratio |e_{n+1}|/|e_n|^2")
    print("  " + "-"*50)
    
    for i in range(min(8, len(seq)-1)):
        e_n = differences[i]
        e_next = differences[i+1]
        if e_n > 0:
            ratio = float(e_next / (e_n ** 2))
            print(f"  {i:2d}  {seq[i]:.10f}  {e_n:.2e}       {ratio:.6f}")
    
    print("\n  Quadratic convergence: |e_{n+1}| ≈ C|e_n|^2")
    print("  Expected for Babylonian/Newton's method")
    
    return differences, cauchy_epsilons

def visualize_convergence(seq, differences):
    """Create visualization of the convergence."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # 1. Sequence values
    ax1 = axes[0, 0]
    n_vals = list(range(len(seq)))
    ax1.plot(n_vals, seq, 'b-o', linewidth=2, markersize=4)
    ax1.axhline(y=math.sqrt(2), color='r', linestyle='--', label=r'$\sqrt{2}$')
    ax1.set_xlabel('Term index n')
    ax1.set_ylabel('$x_n$')
    ax1.set_title(r'Sequence Convergence to $\sqrt{2}$')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 2. Error decay (log scale)
    ax2 = axes[0, 1]
    ax2.semilogy(n_vals, differences, 'r-s', linewidth=2, markersize=5)
    ax2.set_xlabel('Term index n')
    ax2.set_ylabel(r'$|x_n - \sqrt{2}|$ (log scale)')
    ax2.set_title('Error Decay (Quadratic Convergence)')
    ax2.grid(True, alpha=0.3)
    
    # 3. Cauchy property demonstration
    ax3 = axes[1, 0]
    # Compute max differences for different starting indices
    max_diffs = []
    # FIX: Adjusted the range for N_vals to prevent empty iterable for max()
    N_vals = list(range(1, min(15, len(seq) - 1))) # Changed from len(seq) to len(seq) - 1
    #N_vals = list(range(1, min(15, len(seq))))
    for N in N_vals:
        max_diff = max(abs(seq[i] - seq[j]) 
                      for i in range(N, len(seq)) 
                      for j in range(N, len(seq)) 
                      if i < j)
        max_diffs.append(float(max_diff))
    
    ax3.plot(N_vals, max_diffs, 'g-^', linewidth=2, markersize=6)
    ax3.set_xlabel('Starting index N')
    ax3.set_ylabel('max$_{i,j≥N} |x_i - x_j|$')
    ax3.set_title('Cauchy Property: Terms Get Arbitrarily Close')
    ax3.grid(True, alpha=0.3)
    
    # 4. Rational vs real number line
    ax4 = axes[1, 1]
    # Create a number line
    x_vals = np.linspace(1.3, 1.5, 200)
    ax4.axhline(y=0, color='k', linewidth=0.5)
    
    # Mark rational approximations
    for i, term in enumerate(seq[:6]):
        ax4.plot(float(term), 0, 'bo', markersize=8)
        if (float(term)>1.3) and (float(term)<1.5):
            ax4.text(float(term), 0.001, f'$x_{i}$', color='blue', fontsize=9, ha='center')
    
    # Mark √2
    ax4.plot(math.sqrt(2), 0, 'r*', markersize=12, label=r'$\sqrt{2}$ (irrational)')
    
    # Shade rationals
    ax4.axvspan(1.4, 1.42, alpha=0.1, color='blue', label='Rational approximations')
    
    ax4.set_xlim(1.39, 1.43)
    ax4.set_ylim(-0.02, 0.02)
    ax4.set_xlabel('Value on number line')
    ax4.set_title('Rational Approximations vs Irrational Limit')
    ax4.legend(loc='upper right')
    ax4.grid(True, alpha=0.2)
    
    plt.tight_layout()
    plt.savefig('completeness_visualization.png', dpi=150, bbox_inches='tight')
    plt.show(block=False)
    plt.pause(0.001)

def demonstrate_completion():
    """Demonstrate the completion concept explicitly."""
    print("\n" + "="*60)
    print("DEMONSTRATION OF COMPLETION PROCESS")
    print("="*60)
    
    print("\nLet ℚ = {rational numbers}")
    print("Let ℝ = ℚ ∪ {all limit points of Cauchy sequences in ℚ}")
    
    print("\nOur sequence S = {x₀, x₁, x₂, ...} where:")
    print("  x₀ = 1")
    print("  x_{n+1} = (x_n + 2/x_n)/2")
    
    print("\nProperties:")
    print("  1. S ⊂ ℚ (each x_n is rational)")
    print("  2. S is Cauchy: ∀ε>0, ∃N s.t. m,n>N ⇒ |x_m - x_n| < ε")
    print("  3. In ℚ: S has no limit (√2 ∉ ℚ)")
    print("  4. In ℝ: lim S = √2")
    
    print("\nCompletion ℝ = ℚ ∪ {all such 'missing' limits}")
    print("⇒ Every Cauchy sequence in ℝ converges in ℝ")
    print("⇒ ℝ is complete!")

# Main execution
if __name__ == "__main__":
    # Generate sequence
    sequence = babylonian_sqrt_2(n_terms=15)
    
    # Analyze properties
    differences, cauchy_data = analyze_sequence(sequence)
    
    # Visualize
    visualize_convergence(sequence, differences)
    
    # Demonstrate completion concept
    demonstrate_completion()
