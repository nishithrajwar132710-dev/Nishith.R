# 5. Solve z = (x + y)^2 - 2xy
def solve_equation2(x, y):
    z = (x + y) * (x + y) - 2 * x * y
    # This simplifies to: (x + y)^2 - 2xy = x^2 + 2xy + y^2 - 2xy = x^2 + y^2
    print(f"z = (x + y)^2 - 2xy = {z} (which simplifies to x^2 + y^2)")

# Example:
solve_equation2(3, 4)

