import matplotlib.pyplot as plt
import numpy as np


def plot_sin_classic(A, T, t1, d):
    t = np.arange(t1, t1 + d, 0.01)
    y = [(A * np.sin(2 * T * np.pi * i)) for i in t]

    plt.plot(t, y)
    plt.xlabel('time (t)')
    plt.ylabel('value (y)')
    plt.title('Sygnal sinusoidalny')
    plt.grid(True)
    plt.show()


def plot_sin_jednopolowkowy(A, T, t1, d):
    t = np.arange(t1, t1 + d, 0.01)
    y = [0.5 * A * (np.sin(2 * T * np.pi * i) + np.abs((np.sin(2 * T * np.pi * i)))) for i in t]

    plt.plot(t, y)
    plt.xlabel('time (t)')
    plt.ylabel('value (y)')
    plt.title('Sygnal sinusoidalny jednopolowkowy')
    plt.grid(True)
    plt.show()


def plot_sin_dwupolowkowy(A, T, t1, d):
    t = np.arange(t1, t1 + d, 0.01)
    y = [A * np.abs(np.sin(2 * T * np.pi * i)) for i in t]

    plt.plot(t, y)
    plt.xlabel('time (t)')
    plt.ylabel('value (y)')
    plt.title('Sygnal sinusoidalny dwupolowkowy')
    plt.grid(True)
    plt.show()
