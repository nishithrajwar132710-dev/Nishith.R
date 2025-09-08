import numpy as np
import matplotlib.pyplot as plt

# a. Add two sine waves (5 Hz and 10 Hz)
fs1 = 1000
t1 = np.linspace(0, 1, fs1, endpoint=False)
sine_5 = np.sin(2 * np.pi * 5 * t1)
sine_10 = np.sin(2 * np.pi * 10 * t1)
sum_signal = sine_5 + sine_10

plt.figure()
plt.plot(t1, sum_signal)
plt.title('a. Sum of 5 Hz and 10 Hz Sine Waves')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# b. Multiply sine and cosine waves
fs2 = 500
t2 = np.linspace(0, 2, 2 * fs2, endpoint=False)
sine_5b = np.sin(2 * np.pi * 5 * t2)
cos_10b = np.cos(2 * np.pi * 10 * t2)
product = sine_5b * cos_10b

plt.figure()
plt.plot(t2, product)
plt.title('b. Product of 5 Hz Sine and 10 Hz Cosine')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# c. Time shift sine wave
shift = 0.1
sine_orig = np.sin(2 * np.pi * 5 * t1)
sine_shifted = np.sin(2 * np.pi * 5 * (t1 - shift))

plt.figure()
plt.plot(t1, sine_orig, label='Original')
plt.plot(t1, sine_shifted, label='Shifted')
plt.title('c. Time Shifted Sine Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()

# d. Scale amplitude
sine_10d = np.sin(2 * np.pi * 10 * t1)
scaled = 3 * sine_10d

plt.figure()
plt.plot(t1, sine_10d, label='Original')
plt.plot(t1, scaled, label='Scaled')
plt.title('d. Scaled Amplitude of 10 Hz Sine Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()

# e. Reverse signal in time
sine_5e = np.sin(2 * np.pi * 5 * t1)
reversed_signal = sine_5e[::-1]

plt.figure()
plt.plot(t1, sine_5e, label='Original')
plt.plot(t1, reversed_signal, label='Reversed')
plt.title('e. Time-Reversed Sine Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()