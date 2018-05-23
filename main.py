#!/usr/bin/env python

# coding: utf-8
from main_view import BasicView
from signal_generator import *
from sampling import *
import matplotlib.pyplot as plt
import numpy as np
import interpol as ip
import quantization as qz

# basicView = BasicView()
# 10000 probek
signal = simple('sine', 1, 1, 0, 10, 1000)

plt.plot(signal.t_values, signal.values, color="green")
plt.xlabel('time (t)')
plt.ylabel('value (y)')
plt.title('chuj')
plt.grid(True)
# plt.show()

# sampled_signal = sample_signal(signal, 100)

# plt.plot(sampled_signal.t_values, sampled_signal.values, color = "pink")
# plt.xlabel('time (t)')
# plt.ylabel('value (y)')
# plt.title('sampled chuj')
# plt.grid(True)
# plt.show()

# ip_sig_values = sinc_interpolation(sampled_signal.values, sampled_signal.sampling_freq, signal.t_values)
# ip_sig_values = zero_order_hold(sampled_signal.values, sampled_signal.sampling_freq, signal.t_values)
#
#
# plt.plot(signal.t_values, ip_sig_values)
# plt.xlabel('time (t)')
# plt.ylabel('value (y)')
# plt.title('sampled chuj')
# plt.grid(True)
# plt.show()

quant_signal = qz.round_quantize_signal(signal)

plt.plot(quant_signal.t_values, quant_signal.values)
plt.xlabel('time (t)')
plt.ylabel('value (y)')
plt.title('sampled chuj')
plt.grid(True)
plt.show()

