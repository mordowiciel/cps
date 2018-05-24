import numpy as np
from cpssignal import *


def quantize_signal(signal, bits_count):
    y_values = signal.values
    min_y_value = round(np.min(y_values))
    max_y_value = round(np.max(y_values))

    bins = np.linspace(min_y_value, max_y_value, bits_count)
    real_y_values = y_values.astype(float)

    inds = np.digitize(real_y_values, bins)

    print bins[inds[0] - 1]  # lower
    print bins[inds[0]]  # higher

    quantz_values = np.zeros(len(real_y_values))

    for i in range(inds.size):
        index = inds[i]
        value = bins[index - 1]
        quantz_values[i] = value

    return CPSSignal('quantize_signal', signal.t0, signal.t1, signal.sampling_freq, quantz_values)


def round_quantize_signal(signal, bits_count):
    y_values = signal.values
    min_y_value = round(np.min(y_values))
    max_y_value = round(np.max(y_values))

    bins = np.linspace(min_y_value, max_y_value, bits_count)
    real_y_values = y_values.astype(float)

    inds = np.digitize(real_y_values, bins)

    quantz_values = np.zeros(len(real_y_values))

    for i in range(inds.size):
        index = inds[i]
        value = bins[index - 1]

        if value == 0:
            quantz_values[i] = 0.0
            continue

        if index >= bins.size:
            value2 = value
        else:
            value2 = bins[index]

        quantz_values[i] = (value + value2) / 2.0

    return CPSSignal('quantize_signal', signal.t0, signal.t1, signal.sampling_freq, quantz_values)
