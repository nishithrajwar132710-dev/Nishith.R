# -*- coding: utf-8 -*-
"""
Created on Tue Aug  5 10:04:14 2025

@author: LENOVO
"""

def list_to_integer(lst):
    return int(''.join(map(str, lst)))

# Example usage
numbers = [1, 2, 3, 4]
print("Single integer:", list_to_integer(numbers))
