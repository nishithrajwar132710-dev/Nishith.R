# -*- coding: utf-8 -*-
"""
Created on Tue Aug  5 09:55:01 2025

@author: LENOVO
"""

def remove_duplicates(lst):
    return list(set(lst))

# Example usage
items = [1, 2, 2, 3, 4, 4, 5]
print("Without duplicates:", remove_duplicates(items))
