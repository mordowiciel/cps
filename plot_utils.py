import matplotlib.pyplot as plt
import numpy as np


def plot_signal(signal, title):
    t_step = 1.0 / signal.sampling_freq
    t = np.arange(signal.t0, signal.t1, t_step)

    return [t, signal.values]


def plot_histogram(signal, title):
    return [signal.values]
