import matplotlib.pyplot as plt
import numpy as np


def plot_prostokatny(A, T, kW, t1, d):
    t = np.arange(t1, t1 + d, 0.01)
    y = []

    impulse_time = kW * T

    for dt in t:

        temp_t = dt % T

        if temp_t <= impulse_time:
            y_val = A

        else:
            y_val = 0

        y.append(y_val)

    plt.plot(t, y)
    plt.xlabel('time (t)')
    plt.ylabel('value (y)')
    plt.title('Szum gaussowski')
    plt.grid(True)
    plt.show()


def plot_prostokatny_symetryczny(A, T, kW, t1, d):
    t = np.arange(t1, t1 + d, 0.01)
    y = []

    impulse_time = kW * T

    for dt in t:

        temp_t = dt % T

        if temp_t <= impulse_time:
            y_val = A

        else:
            y_val = -A

        y.append(y_val)

    plt.plot(t, y)
    plt.xlabel('time (t)')
    plt.ylabel('value (y)')
    plt.title('Szum gaussowski')
    plt.grid(True)
    plt.show()


def plot_trojkatny(A, T, kW, t1, d):
    t = np.arange(t1, t1 + d, 0.01)
    y = []

    impulse_time = kW * T

    for dt in t:

        temp_t = dt % T

        if temp_t <= impulse_time:

            y_val = (A / (kW * T)) * (temp_t)

        else:
            y_val = (-A / (T * (1 - kW))) * (temp_t) + A / (1 - kW)

        y.append(y_val)

    plt.plot(t, y)
    plt.xlabel('time (t)')
    plt.ylabel('value (y)')
    plt.title('Szum gaussowski')
    plt.grid(True)
    plt.show()
