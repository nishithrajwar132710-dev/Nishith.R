# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 20:23:16 2025

@author: LENOVO
"""

import numpy as np

# a. Create a 3x3 matrix with values from 2 to 10
a = np.arange(2, 11).reshape(3, 3)
print("a:\n", a)

# b. Reverse an array
b = np.array([1, 2, 3, 4, 5])
b_reversed = b[::-1]
print("b reversed:", b_reversed)

# c. Find common values between two arrays
c1 = np.array([1, 2, 3, 4])
c2 = np.array([3, 4, 5, 6])
common = np.intersect1d(c1, c2)
print("common:", common)

# d. Repeat array elements
d = np.array([1, 2, 3])
d_repeated = np.repeat(d, 2)
print("d repeated:", d_repeated)

# e. Find memory size of a NumPy array
e = np.array([1, 2, 3])
print("memory size:", e.nbytes)

# f. Create an array of ones and zeros
f_zeros = np.zeros(5)
f_ones = np.ones(5)
print("zeros:", f_zeros)
print("ones:", f_ones)

# g. Find the 4th element of a specified array
g = np.array([10, 20, 30, 40, 50])
print("4th element:", g[3])
