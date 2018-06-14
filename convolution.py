import numpy as np


def calculate_convolution(arr1, arr2):
    convolution_vector_size = len(arr1) + len(arr2) - 1

    result = []
    for i in range(0, convolution_vector_size):
        value = calculate_next_convolution(i, arr1, arr2)
        result.append(value)

    return np.array(result)


def calculate_next_convolution(convolution_idx, arr1, arr2):
    result = 0.0

    for i in range(0, len(arr1)):
        second_signal_probe_idx = convolution_idx + i
        if second_signal_probe_idx < 0:
            break
        if second_signal_probe_idx > len(arr2) - 1:
            continue
        result += arr1[i] * arr2[second_signal_probe_idx]

    return result
