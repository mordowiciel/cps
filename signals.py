import matplotlib.pyplot as plt
import numpy as np


def plot_prostokatny(A, T, kW):
    t = np.arange(0.0, 10.0, 0.01)
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
