import numpy as np
import utils


def plot_sin_classic(A, T, t1, d):
    t = np.arange(t1, t1 + d, 0.01)
    y = [(A * np.sin(2 * T * np.pi * i)) for i in t]

    utils.plot_signal(t, y, 'Sinusoidalny')
    return y


def plot_sin_jednopolowkowy(A, T, t1, d):
    t = np.arange(t1, t1 + d, 0.01)
    y = [0.5 * A * (np.sin(2 * T * np.pi * i) + np.abs((np.sin(2 * T * np.pi * i)))) for i in t]

    utils.plot_signal(t, y, 'Sinusoidalny jednopolowkowy')
    return y


def plot_sin_dwupolowkowy(A, T, t1, d):
    t = np.arange(t1, t1 + d, 0.01)
    y = [A * np.abs(np.sin(2 * T * np.pi * i)) for i in t]

    utils.plot_signal(t, y, 'Sinusoidalny dwupolowkowy')
    return y

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

    utils.plot_signal(t, y, 'Prostokatny')
    return y


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

    utils.plot_signal(t, y, 'Prostokatny symetryczny')
    return y


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

    utils.plot_signal(t, y, 'Trojkatny')
    return y
