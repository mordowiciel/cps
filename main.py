import matplotlib.pyplot as plt
import numpy as np

# sygnal sinusoidalny

f = 1
t = np.arange(0.0, 3.0, 0.01)
y = np.sin(2 * f * np.pi * t)

y = [(np.sin(2 * f * np.pi * i)) for i in t]
plt.plot(t, y)

plt.xlabel('time (t)')
plt.ylabel('value (y)')
plt.title('Sygnal sinusoidalny')
plt.grid(True)
plt.show()

# sygnal sinusoidalny wyprostowany jednopolowkowo

f = 1
t = np.arange(0.0, 3.0, 0.01)
y = []

for i in t:
    y_val = np.sin(2 * f * np.pi * i)
    if y_val < 0:
        y_val = 0
    y.append(y_val)

plt.plot(t, y)
plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('voltage (mV) vs. time (sec)')
plt.grid(True)
plt.show()

# sygnal sinusoidalny wyprostowany dwupolowkowo
f = 1
t = np.arange(0.0, 3.0, 0.01)
y = []

for i in t:
    y_val = np.abs(np.sin(2 * f * np.pi * i))
    y.append(y_val)

plt.plot(t, y)
plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('voltage (mV) vs. time (sec)')
plt.grid(True)
plt.show()
