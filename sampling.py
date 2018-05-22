from cpssignal import *
import numpy as np


def sample_signal(signal, sampling_val):
    new_values = signal.values[::sampling_val]
    return CPSSignal(signal.name, signal.t0, signal.t1, signal.sampling_freq / sampling_val, new_values)


# TODO : dziwny bug do fixniecia
def zero_order_hold(sampled_y_values, sampled_sampling_freq, x_to_upsample):

    T = 1.0 / sampled_sampling_freq
    new_y_values = []

    for t in x_to_upsample:
        sum_inp = 0
        for index, value in enumerate(sampled_y_values):
            rect_val = rect((t - (T / 2.0) - (index * T)) / T)
            sum_inp += value * rect_val
        new_y_values.append(sum_inp)

    return np.array(new_y_values)


def first_order_hold(sampled_y_values, sampled_sampling_freq, x_to_upsample):
    T = 1.0 / sampled_sampling_freq
    new_y_values = []

    for t in x_to_upsample:
        sum_inp = 0
        for index, value in enumerate(sampled_y_values):
            tri_val = tri((t - index * T) / T)
            sum_inp += value * tri_val
        new_y_values.append(sum_inp)

    return np.array(new_y_values)


def sinc_interpolation(sampled_y_values, sampled_sampling_freq, x_to_upsample):
    T = 1.0 / sampled_sampling_freq
    new_y_values = []

    for t in x_to_upsample:
        sum_inp = 0
        for index, value in enumerate(sampled_y_values):
            sum_inp += value * np.sinc((t / T) - index)
        new_y_values.append(sum_inp)

    return np.array(new_y_values)


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
