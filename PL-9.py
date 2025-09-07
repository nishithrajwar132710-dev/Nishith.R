import pandas as pd
import numpy as np

# ========== a. Arithmetic Operations on Two Series ==========
print("=== a. Add, Subtract, Multiply, Divide Two Series ===")
s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([1, 2, 3, 4])

print("Series 1:\n", s1)
print("Series 2:\n", s2)

print("Addition:\n", s1 + s2)
print("Subtraction:\n", s1 - s2)
print("Multiplication:\n", s1 * s2)
print("Division:\n", s1 / s2)

# ========== b. Convert Dictionary to Pandas Series ==========
print("\n=== b. Dictionary to Series ===")
my_dict = {'a': 100, 'b': 200, 'c': 300}
series_from_dict = pd.Series(my_dict)
print(series_from_dict)

# ========== c. Create Series from List, NumPy Array, and Dictionary ==========
print("\n=== c. Series from List, NumPy Array, and Dictionary ===")

# From list
my_list = [10, 20, 30]
series_from_list = pd.Series(my_list)
print("From List:\n", series_from_list)

# From NumPy array
my_array = np.array([40, 50, 60])
series_from_array = pd.Series(my_array)
print("From NumPy Array:\n", series_from_array)

# From dictionary
my_dict2 = {'x': 100, 'y': 200, 'z': 300}
series_from_dict2 = pd.Series(my_dict2)
print("From Dictionary:\n", series_from_dict2)

# ========== d. Stack Two Series Vertically and Horizontally ==========
print("\n=== d. Stack Two Series ===")
s3 = pd.Series([1, 2, 3])
s4 = pd.Series([4, 5, 6])

# Vertical stack (one below the other)
vertical = pd.concat([s3, s4], ignore_index=True)
print("Vertical Stack:\n", vertical)

# Horizontal stack (side by side as columns)
horizontal = pd.concat([s3, s4], axis=1)
print("Horizontal Stack:\n", horizontal)
