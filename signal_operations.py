import numpy as np
import plot_utils


def add_signals(y1, y2, t):
    y_sum = np.add(y1, y2)
    plot_utils.plot_signal(t, y_sum, 'Adding signals')
    return y_sum


def substract_signals(y1, y2, t):
    y_sub = np.subtract(y1, y2)
    plot_utils.plot_signal(t, y_sub, 'Substracting signals')
    return y_sub


def multiply_signals(y1, y2, t):
    y_mul = np.multiply(y1, y2)
    plot_utils.plot_signal(t, y_mul, 'Multiplying signals')
    return y_mul


def divide_signals(y1, y2, t):
    y_div = np.divide(y1, y2)
    plot_utils.plot_signal(t, y_div, 'Dividing signals')
    return y_div
