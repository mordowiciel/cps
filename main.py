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
import convolution
import correlation


# ### SPLOT SYGNALOW ###
#
# sig_sin = full_wave_rect_sine('sine', 5, 1, 0, 10, 10000)
# sig_square = square('square', 5, 1, 0.5, 0, 10, 10000)
# sig_conv = convolution.calculate_convolution(sig_sin, sig_square)
#
# plt.plot(sig_conv.t_values, sig_conv.values, color="blue")
# plt.xlabel('time (t)')
# plt.ylabel('value (y)')
# plt.title('chuj')
# plt.grid(True)
# plt.show()

# # ### FILTROWANIE SYGNALU ###
# sig_sin = sine('sine', 5, 1, 0, 10, 10000)
# filtered_sig = filter.filtered_hanning_lowpass(sig_sin, 1000, 10)
#
# plt.plot(sig_sin.t_values, sig_sin.values, color="blue")
# plt.xlabel('time (t)')
# plt.ylabel('value (y)')
# plt.title('chuj')
# plt.grid(True)
#
# plt.plot(filtered_sig.t_values, filtered_sig.values, color="green")
# plt.xlabel('time (t)')
# plt.ylabel('value (y)')
# plt.title('chuj')
# plt.grid(True)
# plt.show()
#
# KORELACJA SYGNALU #

# sig_sin = square('sine', 5, 1, 0.1, 0, 10, 50)
# sig_trian = triangular('trian', 5, 1, 0.5, 0, 10, 50)
#
# sig_corr_conv = correlation.calculate_correlation_by_convolution(sig_sin, sig_trian)
# sig_corr_classic = correlation.calculate_classic_correlation(sig_sin, sig_trian)
#
# plt.figure()
# plt.plot(sig_sin.t_values, sig_sin.values, color="green")
# plt.xlabel('time (t)')
# plt.ylabel('value (y)')
# plt.title('chuj')
# plt.grid(True)
#
# plt.plot(sig_trian.t_values, sig_trian.values, color="blue")
# plt.xlabel('time (t)')
# plt.ylabel('value (y)')
# plt.title('chuj')
# plt.grid(True)
#
# plt.figure()
# plt.plot(sig_corr_classic.t_values, sig_corr_classic.values, color="orange")
# plt.xlabel('time (t)')
# plt.ylabel('value (y)')
# plt.title('chuj')
# plt.grid(True)
#
# plt.figure()
# plt.plot(sig_corr_conv.t_values, sig_corr_conv.values, color="orange")
# plt.xlabel('time (t)')
# plt.ylabel('value (y)')
# plt.title('chuj')
# plt.grid(True)
# plt.show()

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
