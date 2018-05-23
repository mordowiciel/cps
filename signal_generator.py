import numpy as np
from cpssignal import CPSSignal
import signal_serializer


def sine(name, A, T, t1, d, sampling_freq):
    sampling_step = 1.0 / sampling_freq

    t = np.arange(t1, t1 + d + sampling_step, sampling_step)
    y = np.array([(A * np.sin(2 * T * np.pi * i)) for i in t], dtype=complex)

    return CPSSignal(name, t1, t1 + d, sampling_freq, y)


def half_wave_rect_sine(name, A, T, t1, d, sampling_freq):
    sampling_step = 1.0 / sampling_freq

    t = np.arange(t1, t1 + d + sampling_step, sampling_step)
    y = np.array([0.5 * A * (np.sin(2 * T * np.pi * i) + np.abs((np.sin(2 * T * np.pi * i)))) for i in t],
                 dtype=complex)

    return CPSSignal(name, t1, t1 + d, sampling_freq, y)


def full_wave_rect_sine(name, A, T, t1, d, sampling_freq):
    sampling_step = 1.0 / sampling_freq

    t = np.arange(t1, t1 + d + sampling_step, sampling_step)
    y = np.array([A * np.abs(np.sin(2 * T * np.pi * i)) for i in t], dtype=complex)

    return CPSSignal(name, t1, t1 + d, sampling_freq, y)


def square(name, A, T, kW, t1, d, sampling_freq):
    sampling_step = 1.0 / sampling_freq

    t = np.arange(t1, t1 + d + sampling_step, sampling_step)
    y = np.zeros(len(t), dtype=complex)

    impulse_time = kW * T

    for counter, dt in enumerate(t):

        temp_t = dt % T

        if temp_t <= impulse_time:
            y_val = A

        else:
            y_val = 0

        y[counter] = y_val

    return CPSSignal(name, t1, t1 + d, sampling_freq, y)


def square_symmetrical(name, A, T, kW, t1, d, sampling_freq):
    sampling_step = 1.0 / sampling_freq

    t = np.arange(t1, t1 + d + sampling_step, sampling_step)
    y = np.zeros(len(t), dtype=complex)

    impulse_time = kW * T

    for counter, dt in enumerate(t):

        temp_t = dt % T

        if temp_t <= impulse_time:
            y_val = A

        else:
            y_val = -A

        y[counter] = y_val

    return CPSSignal(name, t1, t1 + d, sampling_freq, y)


def triangular(name, A, T, kW, t1, d, sampling_freq):
    sampling_step = 1.0 / sampling_freq

    t = np.arange(t1, t1 + d + sampling_step, sampling_step)
    y = np.zeros(len(t), dtype=complex)

    impulse_time = kW * T

    for index, dt in enumerate(t):

        temp_t = dt % T

        if temp_t <= impulse_time:

            y_val = (A / (kW * T)) * (temp_t)

        else:
            y_val = (-A / (T * (1 - kW))) * (temp_t) + A / (1 - kW)

        y[index] = y_val

    return CPSSignal(name, t1, t1 + d, sampling_freq, y)


def step_function(name, A, t1, d, tS, sampling_freq):
    sampling_step = 1.0 / sampling_freq

    t = np.arange(t1, t1 + d + sampling_step, sampling_step)
    y = np.zeros(len(t), dtype=complex)

    for index, dt in enumerate(t):

        if dt > tS:
            y_val = A

        if dt == tS:
            y_val = 1.0 / 2.0 * A

        if dt < tS:
            y_val = 0

        y[index] = y_val

    return CPSSignal(name, t1, t1 + d, sampling_freq, y, discret=True)


def simple_kronecker(n):
    if n == 0:
        return 1.0
    else:
        return 0.0


def kronecker(name, A, nS, n1, l, sampling_freq):

    sampling_step = 1.0 / sampling_freq

    t = np.arange(n1, n1 + l + sampling_step, sampling_step)
    y = np.zeros(len(t), dtype=complex)

    for index, dt in enumerate(t):
        fun_val = dt - nS
        y_val = A * (simple_kronecker(fun_val))
        y[index] = y_val

    return CPSSignal(name, n1, n1 + l, sampling_freq, y, discret=True)


def simple(name, A, T, t1, d, sampling_freq):

    sampling_step = 1.0 / sampling_freq

    t = np.arange(t1, t1 + d + sampling_step, sampling_step)
    y = np.array([(A * i) for i in t], dtype=complex)

    return CPSSignal(name, t1, t1 + d, sampling_freq, y)
