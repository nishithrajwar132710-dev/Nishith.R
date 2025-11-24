import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def z_transform_unit_step():
    """
    Z-transform of unit step u[n] is 1 / (1 - z^{-1}) for |z| > 1.
    """
    # Unit step sequence: u[n] = 1 for n >= 0
    n = np.arange(0, 20)
    u = np.ones_like(n)
    
    # Compute Z-transform numerically (for visualization)
    # We'll just print the known transform
    print("Z-transform of unit step: X(z) = 1 / (1 - z^{-1}), |z| > 1")
    return "1 / (1 - z^{-1})"

def check_stability(H_num, H_den):
    """
    Check stability of H(z) = H_num / H_den.
    Stability: All poles inside unit circle.
    """
    poles = np.roots(H_den)
    print("Poles:", poles)
    
    # Magnitude of poles
    mag_poles = np.abs(poles)
    print("Magnitude of poles:", mag_poles)
    
    if all(mag < 1 for mag in mag_poles):
        return "Stable"
    else:
        return "Unstable"

# Example usage
if __name__ == "__main__":
    # 1. Z-transform of unit step
    print("--- Z-transform of Unit Step ---")
    z_transform_unit_step()
    
    # 2. Check stability for example H(z) = 1 / (1 - 1.5z^{-1})
    print("\n--- Stability Check ---")
    # H(z) = 1 / (1 - a*z^{-1}) -> denominator [1, -a] for [z^0, z^{-1}]
    # Example 1: Stable system a=0.5
    H_num = [1]    # numerator coefficients
    H_den = [1, -0.5]  # denominator coefficients [1, -a]
    
    print("Example 1: H(z) = 1 / (1 - 0.5z^{-1})")
    result1 = check_stability(H_num, H_den)
    print("System is:", result1)
    
    # Example 2: Unstable system a=1.5
    H_den_unstable = [1, -1.5]
    print("\nExample 2: H(z) = 1 / (1 - 1.5z^{-1})")
    result2 = check_stability(H_num, H_den_unstable)
    print("System is:", result2)
