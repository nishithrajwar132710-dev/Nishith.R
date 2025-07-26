# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 17:48:28 2025

@author: LENOVO
"""

# factorial.py

def factorial(n):
    if n < 0:
        return "Invalid input: Negative number"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage
num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")
