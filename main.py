#!/usr/bin/env python

# coding: utf-8
from main_view import BasicView
from signal_generator import *
from sampling import *
import matplotlib.pyplot as plt
import numpy as np
import quantization as qz
import sampling_quantz_util as squ

basicView = BasicView()
# 10000 probek
# signal = sine('sine', 5, 1, 0, 10, 10000)
# #
# # plt.plot(signal.t_values, signal.values, color="green")
# # plt.xlabel('time (t)')
# # plt.ylabel('value (y)')
# # plt.title('chuj')
# # plt.grid(True)
# # plt.show()

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

