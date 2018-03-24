import matplotlib.pyplot as plt
import numpy as np


def plot_sin_classic(f):
    f = 1
    t = np.arange(0.0, 3.0, 0.01)
    y = [(np.sin(2 * f * np.pi * i)) for i in t]

    plt.plot(t, y)
    plt.xlabel('time (t)')
    plt.ylabel('value (y)')
    plt.title('Sygnal sinusoidalny')
    plt.grid(True)
    plt.show()


def plot_sin_jednopolowkowy(f):
    f = 1
    t = np.arange(0.0, 3.0, 0.01)
    y = [0.5 * (np.sin(2 * f * np.pi * i) + np.abs((np.sin(2 * f * np.pi * i)))) for i in t]

    plt.plot(t, y)
    plt.xlabel('time (t)')
    plt.ylabel('value (y)')
    plt.title('Sygnal sinusoidalny jednopolowkowy')
    plt.grid(True)
    plt.show()


def plot_sin_dwupolowkowy(f):
    f = 1
    t = np.arange(0.0, 3.0, 0.01)
    y = [np.abs(np.sin(2 * f * np.pi * i)) for i in t]

    plt.plot(t, y)
    plt.xlabel('time (t)')
    plt.ylabel('value (y)')
    plt.title('Sygnal sinusoidalny dwupolowkowy')
    plt.grid(True)
    plt.show()
