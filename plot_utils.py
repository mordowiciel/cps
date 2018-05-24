import matplotlib.pyplot as plt
import numpy as np


def plot_signal(signal, title):
    t_step = 1.0 / signal.sampling_freq

    t = np.arange(signal.t0, signal.t1 + 1.0 / signal.sampling_freq, 1.0 / signal.sampling_freq)
    return [t, signal.values]


def plot_histogram(signal, title):
    return [signal.values]
