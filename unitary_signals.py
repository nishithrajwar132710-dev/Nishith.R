# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 14:40:16 2025

@author: LENOVO
"""

# unitary_signals.py
# Student: Nishith Rajwar
# Simple signals: step, impulse, ramp

import numpy as np
import matplotlib.pyplot as plt

def unit_step(n):
    # make a unit step signal
    sig = np.zeros(n)
    for i in range(n):
        if i >= 0:
            sig[i] = 1
    plt.stem(sig)
    plt.title("Unit Step Signal u[n]")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return sig

def unit_impulse(n):
    # make unit impulse
    sig = np.zeros(n)
    if n > 0:
        sig[0] = 1
    plt.stem(sig)
    plt.title("Unit Impulse δ[n]")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return sig

def ramp_signal(n):
    # make ramp signal 0,1,2,...
    sig = np.zeros(n)
    for i in range(n):
        sig[i] = i
    plt.stem(sig)
    plt.title("Ramp Signal r[n]")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return sig
