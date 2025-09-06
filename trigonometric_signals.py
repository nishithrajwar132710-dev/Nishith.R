# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 14:40:36 2025

@author: LENOVO
"""

# trigonometric_signals.py
# Student: Nishith Rajwar
# sine, cosine, exponential signals

import numpy as np
import matplotlib.pyplot as plt

def sine_wave(A, f, phi, t):
    sig = A * np.sin(2 * np.pi * f * t + phi)
    plt.plot(t, sig)
    plt.title("Sine Wave")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return sig

def cosine_wave(A, f, phi, t):
    sig = A * np.cos(2 * np.pi * f * t + phi)
    plt.plot(t, sig)
    plt.title("Cosine Wave")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return sig

def exponential_signal(A, a, t):
    sig = A * np.exp(a * t)
    plt.plot(t, sig)
    plt.title("Exponential Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return sig
