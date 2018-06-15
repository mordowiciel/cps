import numpy as np
from cpssignal import CPSSignal


def calculate_convolution_arr(arr1, arr2):
    result = np.convolve(arr1, arr2)
    return result


def calculate_convolution(sig1, sig2):
    result = np.convolve(sig1.values, sig2.values)
    return CPSSignal('convolved', sig1.t0, sig1.t1, sig1.sampling_freq, result)


def calculate_next_convolution(convolution_idx, sig1, sig2):
    result = 0.0

    for i in range(0, len(sig1.values)):
        second_signal_probe_idx = convolution_idx + i
        if second_signal_probe_idx < 0:
            break
        if second_signal_probe_idx > len(sig2.values) - 1:
            continue
        result += sig1.values[i] * sig2.values[second_signal_probe_idx]

    return result
