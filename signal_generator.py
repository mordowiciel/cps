import numpy as np
from cpssignal import CPSSignal
import signal_serializer


def sine(A, T, t1, d, sampling_freq):
    sampling_step = 1.0 / sampling_freq

    t = np.arange(t1, t1 + d, sampling_step)
    y = np.array([(A * np.sin(2 * T * np.pi * i)) for i in t], dtype=complex)

    return CPSSignal(t1, t1 + d, sampling_freq, y)


def half_wave_rect_sine(A, T, t1, d, sampling_freq):
    t = np.arange(t1, t1 + d, sampling_freq)
    y = np.array([0.5 * A * (np.sin(2 * T * np.pi * i) + np.abs((np.sin(2 * T * np.pi * i)))) for i in t],
                 dtype=complex)

    return CPSSignal(t1, t1 + d, sampling_freq, y)


def full_wave_rect_sine(A, T, t1, d, sampling_freq):
    t = np.arange(t1, t1 + d, sampling_freq)
    y = np.array([A * np.abs(np.sin(2 * T * np.pi * i)) for i in t], dtype=complex)

    return CPSSignal(t1, t1 + d, sampling_freq, y)


def square(A, T, kW, t1, d, sampling_freq):
    t = np.arange(t1, t1 + d, sampling_freq)
    y = np.zeros(len(t), dtype=complex)

    impulse_time = kW * T

    for counter, dt in enumerate(t):

        temp_t = dt % T

        if temp_t <= impulse_time:
            y_val = A

        else:
            y_val = 0

        y[counter] = y_val

    return CPSSignal(t1, t1 + d, sampling_freq, y)


def square_symmetrical(A, T, kW, t1, d, sampling_freq):
    t = np.arange(t1, t1 + d, sampling_freq)
    y = np.zeros(len(t), dtype=complex)

    impulse_time = kW * T

    for counter, dt in enumerate(t):

        temp_t = dt % T

        if temp_t <= impulse_time:
            y_val = A

        else:
            y_val = -A

        y[counter] = y_val

    return CPSSignal(t1, t1 + d, sampling_freq, y)


def triangular(A, T, kW, t1, d, sampling_freq):
    t = np.arange(t1, t1 + d, sampling_freq)
    y = np.zeros(len(t), dtype=complex)

    impulse_time = kW * T

    for index, dt in enumerate(t):

        temp_t = dt % T

        if temp_t <= impulse_time:

            y_val = (A / (kW * T)) * (temp_t)

        else:
            y_val = (-A / (T * (1 - kW))) * (temp_t) + A / (1 - kW)

        y[index] = y_val

    return CPSSignal(t1, t1 + d, sampling_freq, y)


def init_first_app_state():
    sig_sine = sine(A=2, T=1, t1=0, d=1, sampling_freq=100)
    sig_half_sine = half_wave_rect_sine(A=2, T=1, t1=0, d=1, sampling_freq=100)
    sig_full_sine = full_wave_rect_sine(A=2, T=1, t1=0, d=1, sampling_freq=100)
    sig_square = square(A=5, T=1, kW=0.5, t1=0, d=10, sampling_freq=100)
    sig_square_symm = square_symmetrical(A=5, T=1, kW=0.5, t1=0, d=10, sampling_freq=100)
    sig_triangular = triangular(A=5, T=1, kW=0.5, t1=0, d=10, sampling_freq=100)

    signal_serializer.serialize_signal(sig_sine, 'sine')
    signal_serializer.serialize_signal(sig_half_sine, 'half_wave_rectified_sine')
    signal_serializer.serialize_signal(sig_full_sine, 'full_wave_rectified_sine')
    signal_serializer.serialize_signal(sig_square, 'square')
    signal_serializer.serialize_signal(sig_square_symm, 'square_symmetrical')
    signal_serializer.serialize_signal(sig_triangular, 'triangular')
