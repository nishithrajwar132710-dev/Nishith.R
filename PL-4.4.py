# -*- coding: utf-8 -*-
"""
Created on Tue Aug  5 10:03:18 2025

@author: LENOVO
"""

from collections import Counter

def frequency(lst):
    return dict(Counter(lst))

# Example usage
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
print("Frequency:", frequency(items))
