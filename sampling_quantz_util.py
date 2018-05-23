from math import *
import numpy as np


def mse(quant_values, signal_values):
    mse_sum = 0.0

    for n in range(len(quant_values)):
        mse_sum += pow(signal_values[n] - quant_values[n], 2)

    return (1.0 / len(quant_values)) * mse_sum


def snr(quant_values, signal_values):
    numerator_sum = 0.0
    for n in range(len(quant_values)):
        numerator_sum += pow(quant_values[n], 2)

    denominator_sum = 0.0
    for n in range(len(quant_values)):
        denominator_sum += pow(signal_values[n] - quant_values[n], 2)

    res = 10.0 * log10(numerator_sum / denominator_sum)
    return res


def psnr(quant_values, signal_values):
    return 10.0 * log10(np.max(signal_values) / mse(quant_values, signal_values))


def md(quant_values, signal_values):
    md_val = 0.0
    for n in range(len(quant_values)):
        temp_md_val = abs(signal_values[n] - quant_values[n])
        if temp_md_val > md_val:
            md_val = temp_md_val
    return md_val