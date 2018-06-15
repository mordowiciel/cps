import numpy as np
import convolution
from cpssignal import CPSSignal


def calculate_classic_correlation(sig1, sig2):
    sig1_vals = sig1.values
    sig2_vals = sig2.values

    corr_result = calculate_correlation(sig1_vals, sig2_vals)
    return CPSSignal('correlated', sig1.t0, sig1.t1, sig1.sampling_freq, corr_result)


def calculate_correlation(arr1, arr2):
    correlation_vector_size = len(arr1) + len(arr2) - 1
    index_offset = -(len(arr2) - 1)
    result = []
    for i in range(0, correlation_vector_size):
        index = i + index_offset
        value = calculate_next_correlation(index, arr1, arr2)
        result.append(value)

    return np.array(result)


def calculate_next_correlation(correlation_idx, arr1, arr2):
    result = 0.0

    for i in range(0, len(arr1)):
        second_signal_probe_idx = correlation_idx + i
        if second_signal_probe_idx < 0:
            continue
        if second_signal_probe_idx > len(arr2) - 1:
            break
        result += arr1[i] * arr2[second_signal_probe_idx]

    return result


def calculate_correlation_by_convolution(sig1, sig2):
    sig2.values = np.flipud(sig2.values)
    return convolution.calculate_convolution(sig1, sig2)
