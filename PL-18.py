import numpy as np
import matplotlib.pyplot as plt

# Sample signals
x = np.array([1, 2, 3, 4])
h = np.array([1, 0, -1])

# Linear convolution
lin_conv = np.convolve(x, h)
print("Linear convolution result:", lin_conv)
plt.show()

# Circular convolution (length = max length of x and h)
N = max(len(x), len(h))
X = np.fft.fft(x, n=N)
H = np.fft.fft(h, n=N)
circ_conv = np.fft.ifft(X * H).real
print("Circular convolution result:", circ_conv)
plt.show()

# Plotting
plt.figure(figsize=(10,5))
plt.stem(lin_conv, linefmt='b-', markerfmt='bo', label='Linear Convolution', use_line_collection=True)
plt.stem(circ_conv, linefmt='r--', markerfmt='rx', label='Circular Convolution', use_line_collection=True)
plt.title('Linear vs Circular Convolution')
plt.xlabel('Index')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()





import numpy as np
import matplotlib.pyplot as plt

# Generate noisy sinusoidal signal
fs = 500  # Sampling frequency
t = np.linspace(0, 1, fs)
freq = 5  # frequency of sinusoid
signal = np.sin(2 * np.pi * freq * t) + 0.5 * np.random.randn(fs)

# Autocorrelation
autocorr = np.correlate(signal, signal, mode='full')
lags = np.arange(-len(signal) + 1, len(signal))

# Plot signal
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(t, signal)
plt.title('Noisy Sinusoidal Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

# Plot autocorrelation
plt.subplot(1, 2, 2)
plt.plot(lags, autocorr)
plt.title('Autocorrelation')
plt.xlabel('Lag')
plt.ylabel('Correlation')
plt.grid(True)

plt.tight_layout()
plt.show()
