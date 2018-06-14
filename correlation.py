import numpy as np


def calculate_correlation(sig1, sig2):

    sig1_vals = sig1.values
    sig2_vals = np.flipud(sig2.values)

    return np.convolve(sig1_vals, sig2_vals)
