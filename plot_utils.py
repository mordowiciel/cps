import matplotlib.pyplot as plt
import numpy as np


def plot_signal(signal, title):
    t_step = 1.0 / signal.sampling_freq
    t = np.arange(signal.t0, signal.t1, t_step)

    return [t, signal.values]
    # plt.xlabel('time (t)')
    # plt.ylabel('value (y)')
    # plt.title(title)
    # plt.grid(True)
    # plt.show()


def plot_histogram(signal, title):
    # plt.figure(300)

    # plt.xlabel('Value')
    # plt.ylabel('Quantity')
    # plt.title(title)
    return [signal.values]
    plt.hist(signal.values, alpha=0.5, histtype='bar', ec='black')
    # plt.show()
