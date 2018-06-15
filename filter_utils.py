import numpy as np


def calculate_impulse_response(n, k, m):
    if n == ((m - 1) / 2.0):
        return 2.0 / k
    else:
        numerator = np.sin((2.0 * np.pi * (n - ((m - 1) / 2.0))) / k)
        denominator = np.pi * (n - ((m - 1) / 2.0))
        return numerator / denominator


def rectangular_window_response(n, k, m):
    return calculate_impulse_response(n, k, m)


def calculate_K_for_lowpass(sampling_frequency, cutoff_frequency):
    return sampling_frequency / cutoff_frequency


def calculate_K_for_bandpass(sampling_frequency, cutoff_frequency):
    temp_cutoff_freq = cutoff_frequency / 4 - sampling_frequency
    return sampling_frequency / temp_cutoff_freq


def calculate_K_for_highpass(sampling_frequency, cutoff_frequency):
    temp_cutoff_freq = sampling_frequency / 2 - cutoff_frequency
    return sampling_frequency / temp_cutoff_freq


def hamming_window_response(n, k, m):
    return calculate_impulse_response(n, k, m) * calculate_hamming_value(n, m)


def hanning_window_response(n, k, m):
    return calculate_impulse_response(n, k, m) * calculate_hanning_value(n, m)


def blackman_window_response(n, k, m):
    return calculate_impulse_response(n, k, m) * calculate_blackman_value(n, m)


def calculate_hamming_window_response_bandpass(n, k, m):
    return calculate_impulse_response(n, k, m) * calculate_bandpass(n) * calculate_hamming_value(n, m)


def calculate_hanning_window_response_bandpass(n, k, m):
    return calculate_impulse_response(n, k, m) * calculate_bandpass(n) * calculate_hanning_value(n, m)


def calculate_blackman_window_response_bandpass(n, k, m):
    return calculate_impulse_response(n, k, m) * calculate_bandpass(n) * calculate_blackman_value(n, m)


def calculate_hamming_window_response_highpass(n, k, m):
    return calculate_impulse_response(n, k, m) * calculate_high_pass(n) * calculate_hamming_value(n, m)


def calculate_hanning_window_response_highpass(n, k, m):
    return calculate_impulse_response(n, k, m) * calculate_high_pass(n) * calculate_hanning_value(n, m)


def calculate_blackman_window_response_highpass(n, k, m):
    return calculate_impulse_response(n, k, m) * calculate_high_pass(n) * calculate_blackman_value(n, m)


def calculate_bandpass(n):
    return 2 * np.sin(np.pi * n / 2)


def calculate_high_pass(n):
    if n % 2 == 0:
        return 1
    else:
        return -1


def calculate_hamming_value(n, m):
    return 0.53836 - 0.46164 * np.cos(2.0 * np.pi * n / m)


def calculate_hanning_value(n, m):
    return 0.5 - 0.5 * np.cos(2.0 * np.pi * n / m)


def calculate_blackman_value(n, m):
    return 0.42 - 0.5 * np.cos(2.0 * np.pi * n / m) + 0.08 * np.cos(4.0 * np.pi * n / m)
