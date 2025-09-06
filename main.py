# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 14:41:34 2025

@author: LENOVO
"""

# main.py
# Student: Nishith Rajwar
# Test all signals and operations
# For LHC Exam, Marwadi University

import numpy as np
import unitary_signals as us
import trigonometric_signals as ts
import operations as op

# -------- 1. Unitary Signals --------
n = 20
step_sig = us.unit_step(n)
impulse_sig = us.unit_impulse(n)
ramp_sig = us.ramp_signal(n)

# -------- 2. Trig Signals --------
t = np.linspace(0, 1, 500)
sine_sig = ts.sine_wave(2, 5, 0, t)
cos_sig = ts.cosine_wave(2, 5, 0, t)
exp_sig = ts.exponential_signal(2, 3, t)

# -------- 3. Operations --------
shifted_sine = op.time_shift(sine_sig, 5)
scaled_sine = op.time_scale(sine_sig, 2)
added_sig = op.signal_addition(step_sig, ramp_sig)
mult_sig = op.signal_multiplication(sine_sig, cos_sig)

print("All tasks completed! Check plots.")
