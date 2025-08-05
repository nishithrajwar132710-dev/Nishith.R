# -*- coding: utf-8 -*-
"""
Created on Tue Aug  5 09:45:02 2025

@author: LENOVO
"""

def multiply_list(items):
    result = 1
    for item in items:
        result *= item
    return result

# Example usage
numbers = [2, 3, 4]
print("Product:", multiply_list(numbers))
