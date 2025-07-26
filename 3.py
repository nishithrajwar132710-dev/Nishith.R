# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 17:58:13 2025

@author: LENOVO
"""

# fibonacci.py

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example usage
num = int(input("Enter number of terms: "))
print(f"Fibonacci sequence up to {num} terms:")
print(fibonacci(num))
