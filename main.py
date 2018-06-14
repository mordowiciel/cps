#!/usr/bin/env python

# coding: utf-8
from main_view import BasicView
from signal_generator import *
from sampling import *
import matplotlib.pyplot as plt
import numpy as np
import quantization as qz
import sampling_quantz_util as squ
import filter

### SPLOT SYGNALU ###
sig_sin = triangular('sine', 5, 1, 0.5, 0, 10, 44000)

K = filter.calculate_K_for_highpass(sig_sin.sampling_freq, 4400)
num_of_coefficients = 50

window_impulse_response = []

for i in range(0, num_of_coefficients):
    window_impulse_response.append(filter.calculate_blackman_window_response_highpass(i, K, num_of_coefficients))

window_impulse_response = np.array(window_impulse_response)

convolved = np.convolve(sig_sin.values, window_impulse_response)
t_convolved = np.linspace(0, 10, len(convolved))

t_impulse = np.linspace(0, 10, len(window_impulse_response))

print 'sine', len(sig_sin.values)
print 'convolved', len(convolved)

plt.plot(sig_sin.t_values, sig_sin.values, color ="blue")
plt.xlabel('time (t)')
plt.ylabel('value (y)')
plt.title('chuj')
plt.grid(True)

plt.plot(t_convolved, convolved, color="green")
plt.xlabel('time (t)')
plt.ylabel('value (y)')
plt.title('chuj')
plt.grid(True)
plt.show()

# # M-elementowy sygnal h
# sig_sin = half_wave_rect_sine('sine', 5, 1, 0, 10, 10000)
#
# # N-elementowy sygnal x
# sig_sin2 = triangular('sine', 1, 1, 0.5, 0, 10, 10000)
#
# conv_values = np.convolve(sig_sin.values, sig_sin2.values)
#
# t = np.linspace(0, 10, len(sig_sin.values) + len(sig_sin2.values) - 1)

# basicView = BasicView()
# 10000 probek
# signal = sine('sine', 5, 1, 0, 10, 10000)
# #
# plt.plot(signal.t_values, signal.values, color="green")
# plt.xlabel('time (t)')
# plt.ylabel('value (y)')
# plt.title('chuj')
# plt.grid(True)
# plt.show()

# sampled_signal = sample_signal(signal, 2000)

# # plt.plot(sampled_signal.t_values, sampled_signal.values, color = "pink")
# # plt.xlabel('time (t)')
# # plt.ylabel('value (y)')
# # plt.title('sampled chuj')
# # plt.grid(True)
# # plt.show()

# ip_sig = sinc_interpolation(sampled_signal, signal.t_values)

# plt.plot(ip_sig.t_values, ip_sig.values)
# plt.xlabel('time (t)')
# plt.ylabel('value (y)')
# plt.title('sampled chuj')
# plt.grid(True)
# plt.show()

# # # quant_signal = qz.round_quantize_signal(signal)
# # #
# # #
# # # MSE = squ.mse(quant_signal.values, signal.values)
# # # print MSE
# # #
# # # SNR = squ.snr(quant_signal.values, signal.values)
# # # print SNR
# # #
# # # PSNR = squ.psnr(quant_signal.values, signal.values)
# # # print PSNR
# # #
# # # MD = squ.md(quant_signal.values, signal.values)
# # # print MD
# # #
# # # plt.plot(quant_signal.t_values, quant_signal.values)
# # # plt.xlabel('time (t)')
# # # plt.ylabel('value (y)')
# # # plt.title('sampled chuj')
# # # plt.grid(True)
# # # plt.show()
