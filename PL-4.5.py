# -*- coding: utf-8 -*-
"""
Created on Tue Aug  5 10:03:48 2025

@author: LENOVO
"""

def common_items(list1, list2):
    return list(set(list1) & set(list2))

# Example usage
list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6]
print("Common items:", common_items(list_a, list_b))
