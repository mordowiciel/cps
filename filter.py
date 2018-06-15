import numpy as np
import convolution
from cpssignal import CPSSignal
from filter_utils import *


def filtered_blackman_lowpass(sig, cutoff_frequency, num_of_coefficients):
    K = calculate_K_for_lowpass(sig.sampling_freq, cutoff_frequency)
    window_impulse_response = []
    for i in range(0, num_of_coefficients):
        window_impulse_response.append(blackman_window_response(i, K, num_of_coefficients))

    window_impulse_response = np.array(window_impulse_response)
    conv_arr = convolution.calculate_convolution_arr(window_impulse_response, sig.values)
    return CPSSignal('filtered', sig.t0, sig.t1, sig.sampling_freq, conv_arr)


def filtered_blackman_bandpass(sig, cutoff_frequency, num_of_coefficients):
    K = calculate_K_for_bandpass(sig.sampling_freq, cutoff_frequency)
    window_impulse_response = []
    for i in range(0, num_of_coefficients):
        window_impulse_response.append(calculate_blackman_window_response_bandpass(i, K, num_of_coefficients))

    window_impulse_response = np.array(window_impulse_response)
    conv_arr = convolution.calculate_convolution_arr(window_impulse_response, sig.values)
    return CPSSignal('filtered', sig.t0, sig.t1, sig.sampling_freq, conv_arr)


def filtered_blackman_highpass(sig, cutoff_frequency, num_of_coefficients):
    K = calculate_K_for_highpass(sig.sampling_freq, cutoff_frequency)
    window_impulse_response = []
    for i in range(0, num_of_coefficients):
        window_impulse_response.append(calculate_blackman_window_response_highpass(i, K, num_of_coefficients))

    window_impulse_response = np.array(window_impulse_response)
    conv_arr = convolution.calculate_convolution_arr(window_impulse_response, sig.values)
    return CPSSignal('filtered', sig.t0, sig.t1, sig.sampling_freq, conv_arr)


def filtered_hamming_lowpass(sig, cutoff_frequency, num_of_coefficients):
    K = calculate_K_for_lowpass(sig.sampling_freq, cutoff_frequency)
    window_impulse_response = []
    for i in range(0, num_of_coefficients):
        window_impulse_response.append(hamming_window_response(i, K, num_of_coefficients))

    window_impulse_response = np.array(window_impulse_response)
    conv_arr = convolution.calculate_convolution_arr(window_impulse_response, sig.values)
    return CPSSignal('filtered', sig.t0, sig.t1, sig.sampling_freq, conv_arr)


def filtered_hamming_bandpass(sig, cutoff_frequency, num_of_coefficients):
    K = calculate_K_for_bandpass(sig.sampling_freq, cutoff_frequency)
    window_impulse_response = []
    for i in range(0, num_of_coefficients):
        window_impulse_response.append(calculate_hamming_window_response_bandpass(i, K, num_of_coefficients))

    window_impulse_response = np.array(window_impulse_response)
    conv_arr = convolution.calculate_convolution_arr(window_impulse_response, sig.values)
    return CPSSignal('filtered', sig.t0, sig.t1, sig.sampling_freq, conv_arr)


def filtered_hamming_highpass(sig, cutoff_frequency, num_of_coefficients):
    K = calculate_K_for_highpass(sig.sampling_freq, cutoff_frequency)
    window_impulse_response = []
    for i in range(0, num_of_coefficients):
        window_impulse_response.append(calculate_hamming_window_response_highpass(i, K, num_of_coefficients))

    window_impulse_response = np.array(window_impulse_response)
    conv_arr = convolution.calculate_convolution_arr(window_impulse_response, sig.values)
    return CPSSignal('filtered', sig.t0, sig.t1, sig.sampling_freq, conv_arr)


def filtered_hanning_lowpass(sig, cutoff_frequency, num_of_coefficients):
    K = calculate_K_for_lowpass(sig.sampling_freq, cutoff_frequency)
    window_impulse_response = []
    for i in range(0, num_of_coefficients):
        window_impulse_response.append(hanning_window_response(i, K, num_of_coefficients))

    window_impulse_response = np.array(window_impulse_response)
    conv_arr = convolution.calculate_convolution_arr(window_impulse_response, sig.values)
    return CPSSignal('filtered', sig.t0, sig.t1, sig.sampling_freq, conv_arr)


def filtered_hanning_bandpass(sig, cutoff_frequency, num_of_coefficients):
    K = calculate_K_for_bandpass(sig.sampling_freq, cutoff_frequency)
    window_impulse_response = []
    for i in range(0, num_of_coefficients):
        window_impulse_response.append(calculate_hanning_window_response_bandpass(i, K, num_of_coefficients))

    window_impulse_response = np.array(window_impulse_response)
    conv_arr = convolution.calculate_convolution_arr(window_impulse_response, sig.values)
    return CPSSignal('filtered', sig.t0, sig.t1, sig.sampling_freq, conv_arr)


def filtered_hanning_highpass(sig, cutoff_frequency, num_of_coefficients):
    K = calculate_K_for_highpass(sig.sampling_freq, cutoff_frequency)
    window_impulse_response = []
    for i in range(0, num_of_coefficients):
        window_impulse_response.append(calculate_hanning_window_response_highpass(i, K, num_of_coefficients))

    window_impulse_response = np.array(window_impulse_response)
    conv_arr = convolution.calculate_convolution_arr(window_impulse_response, sig.values)
    return CPSSignal('filtered', sig.t0, sig.t1, sig.sampling_freq, conv_arr)
