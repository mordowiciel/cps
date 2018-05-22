#!/usr/bin/env python

# coding: utf-8
from main_view import BasicView
from signal_generator import *
from sampling import *
import matplotlib.pyplot as plt
import numpy as np
import interpol as ip

# basicView = BasicView()
# 10000 probek
signal = sine('sine', 5, 1, 0, 10, 1000)

plt.plot(signal.t_values, signal.values, color="green")
plt.xlabel('time (t)')
plt.ylabel('value (y)')
plt.title('chuj')
plt.grid(True)
# plt.show()

sampled_signal = sample_signal(signal, 100)

# plt.plot(sampled_signal.t_values, sampled_signal.values, color = "pink")
# plt.xlabel('time (t)')
# plt.ylabel('value (y)')
# plt.title('sampled chuj')
# plt.grid(True)
# plt.show()

# ip_sig_values = sinc_interpolation(sampled_signal.values, sampled_signal.sampling_freq, signal.t_values)
ip_sig_values = zero_order_hold(sampled_signal.values, sampled_signal.sampling_freq, signal.t_values)


plt.plot(signal.t_values, ip_sig_values)
plt.xlabel('time (t)')
plt.ylabel('value (y)')
plt.title('sampled chuj')
plt.grid(True)
plt.show()

# # generate bins values
# y_values = signal.values
# min_y_value = round(np.min(y_values))
# max_y_value = round(np.max(y_values))
#
# # bins = np.arange(min_y_value, max_y_value + 1.0, 5.0)
# bins = np.array([-5.0, -2.0, 0.0, 2.0, 5.0])
# print bins
#
# real_y_values = y_values.astype(float)
#
# inds = np.digitize(real_y_values, bins)
#
# print bins[inds[0] - 1] # lower
# print bins[inds[0]] #higher
#
# quantz_values = np.zeros(len(real_y_values))
#
#
# # dla kazdego indeksu tablicy w inds:
# # value = bins[index]
#
# for i in range(inds.size):
#     index = inds[i]
#     value = bins[index - 1]
#     quantz_values[i] = value
#
#
# plt.plot(signal.t_values, quantz_values)
# plt.xlabel('time (t)')
# plt.ylabel('value (y)')
# plt.title('sampled chuj')
# plt.grid(True)
# plt.show()

