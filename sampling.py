from cpssignal import *
import numpy as np


def sample_signal(signal, sampling_val):
    new_values = signal.values[::sampling_val]
    return CPSSignal(signal.name, signal.t0, signal.t1, signal.sampling_freq / sampling_val, new_values, origin_signal=signal)


# TODO : dziwny bug do fixniecia
def zero_order_hold(sampled_signal, x_to_upsample):
    T = 1.0 / sampled_signal.sampling_freq
    new_y_values = []

    for t in x_to_upsample:
        sum_inp = 0
        for index, value in enumerate(sampled_signal.values):
            rect_val = rect((t - (T / 2.0) - (index * T)) / T)
            sum_inp += value * rect_val
        new_y_values.append(sum_inp)

    new_sampling_freq = 1.0 / (x_to_upsample[1] - x_to_upsample[0])

    return CPSSignal('zoh_' + sampled_signal.name, x_to_upsample[0], x_to_upsample[-1], new_sampling_freq, new_y_values, origin_signal=sampled_signal)


def first_order_hold(sampled_signal, x_to_upsample):
    T = 1.0 / sampled_signal.sampling_freq
    new_y_values = []

    for t in x_to_upsample:
        sum_inp = 0
        for index, value in enumerate(sampled_signal.values):
            tri_val = tri((t - index * T) / T)
            sum_inp += value * tri_val
        new_y_values.append(sum_inp)

    new_sampling_freq = 1.0 / (x_to_upsample[1] - x_to_upsample[0])

    return CPSSignal('foh_' + sampled_signal.name, x_to_upsample[0], x_to_upsample[-1], new_sampling_freq, new_y_values, origin_signal=sampled_signal)


def sinc_interpolation(sampled_signal, x_to_upsample):
    T = 1.0 / sampled_signal.sampling_freq
    new_y_values = []

    for t in x_to_upsample:
        sum_inp = 0
        for index, value in enumerate(sampled_signal.values):
            sum_inp += value * np.sinc((t / T) - index)
        new_y_values.append(sum_inp)

    new_sampling_freq = 1.0 / (x_to_upsample[1] - x_to_upsample[0])

    return CPSSignal('sinc_' + sampled_signal.name, x_to_upsample[0], x_to_upsample[-1], new_sampling_freq, new_y_values, origin_signal=sampled_signal)


def rect(t):
    if abs(t) > 0.5:
        return 0.0
    if abs(t) == 0.5:
        return 0.5
    if abs(t) < 0.5:
        return 1.0


def tri(t):
    if abs(t) < 1.0:
        return 1.0 - abs(t)
    else:
        return 0.0
