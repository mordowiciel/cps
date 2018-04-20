#!/usr/bin/env python
from main_view import BasicView
import signal_generator
import numpy as np
import matplotlib.pyplot as plt


# import signal_operations
# import plot_utils


# basicView = BasicView()

# signal = signal_generator.step_function('step', A=10, t1=0, d=10, tS=5, sampling_freq=1000)

signal = signal_generator.kronecker('kronecker', A=1, n1=-25.0, nS=0, l=50.0, sampling_freq=2)

t = np.arange(signal.t0, signal.t1, 0.5)

plt.scatter(t, signal.values)
plt.xlabel('time (t)')
plt.ylabel('value (y)')
plt.title('chuj')
plt.grid(True)
plt.show()

# signal_generator.init_first_app_state()

# sig_square = signal_generator.square(A=5, T=1, kW=0.5, t1=0, d=10, sampling_freq=100)
# sig_sine = signal_generator.sine(A=2, T=1, t1=0, d=10, sampling_freq=100)

# sig_sum = signal_operations.divide_signals(sig_sine, sig_square)

# plot_utils.plot_signal(sig_square, 'sig square')
# plot_utils.plot_signal(sig_sine, 'sig sine')
# plot_utils.plot_signal(sig_sum, 'sig sum')
