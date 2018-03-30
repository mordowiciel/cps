import numpy as np


def calculate_average(n1, n2, y):
    sig_sum = 0

    for n in range(n1, n2):
        sig_sum += y[n]

    temp = (1.0 / (n2 - n1 + 1))
    avg = temp * sig_sum

    return avg


def calculate_abs_average(n1, n2, y):
    sig_sum = 0

    for n in range(n1, n2):
        sig_sum += np.abs(y[n])

    temp = (1.0 / (n2 - n1 + 1))
    abs_avg = temp * sig_sum

    return abs_avg


def calculate_avg_power(n1, n2, y):
    sig_sum = 0

    for n in range(n1, n2):
        sig_sum += pow(y[n], 2)

    temp = (1.0 / (n2 - n1 + 1))
    avg_pow = temp * sig_sum

    return avg_pow


def calculate_variance(n1, n2, y):
    sig_sum = 0
    sig_avg = calculate_average(n1, n2, y)

    for n in range(n1, n2):
        sig_sum += pow((y[n] - sig_avg), 2)

    temp = (1.0 / (n2 - n1 + 1))
    var = temp * sig_sum

    return var


def calculate_root_mean_square(n1, n2, y):
    sig_avg_pow = calculate_avg_power(n1, n2, y)
    rms = np.sqrt(sig_avg_pow)

    return rms
