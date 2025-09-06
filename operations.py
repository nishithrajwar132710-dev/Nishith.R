# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 14:41:12 2025

@author: LENOVO
"""

# operations.py
# Student: Nishith Rajwar
# basic signal operations: shift, scale, add, multiply

import numpy as np
import matplotlib.pyplot as plt

def time_shift(sig, k):
    n = len(sig)
    shifted = np.zeros(n)
    if k >= 0:
        shifted[k:] = sig[:n-k]
    else:
        shifted[:n+k] = sig[-k:]
    plt.plot(sig, label="Original")
    plt.plot(shifted, label=f"Shifted by {k}")
    plt.title("Time Shift")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    plt.show()
    return shifted

def time_scale(sig, k):
    n = len(sig)
    scaled_len = n*k
    scaled = np.zeros(scaled_len)
    scaled[::k] = sig
    plt.stem(scaled)
    plt.title(f"Time Scaling by {k}")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return scaled

def signal_addition(sig1, sig2):
    n = max(len(sig1), len(sig2))
    a = np.zeros(n)
    b = np.zeros(n)
    a[:len(sig1)] = sig1
    b[:len(sig2)] = sig2
    res = a + b
    plt.plot(a, label="Sig1")
    plt.plot(b, label="Sig2")
    plt.plot(res, label="Sum", linewidth=2)
    plt.title("Signal Addition")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    plt.show()
    return res

def signal_multiplication(sig1, sig2):
    n = max(len(sig1), len(sig2))
    a = np.zeros(n)
    b = np.zeros(n)
    a[:len(sig1)] = sig1
    b[:len(sig2)] = sig2
    res = a * b
    plt.plot(a, label="Sig1")
    plt.plot(b, label="Sig2")
    plt.plot(res, label="Multiply", linewidth=2)
    plt.title("Signal Multiplication")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    plt.show()
    return res
