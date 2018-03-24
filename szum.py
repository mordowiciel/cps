import matplotlib.pyplot as plt
import numpy as np


def szum_jednostajny():
    t = np.arange(0.0, 3.0, 0.01)
    y = np.random.uniform(-1, 1, len(t))

    plt.plot(t, y)
    plt.xlabel('time (t)')
    plt.ylabel('value (y)')
    plt.title('Szum jednostajny')
    plt.grid(True)
    plt.show()


def szum_gaussowski():
    t = np.arange(0.0, 3.0, 0.01)
    y = np.random.normal(-1, 1, len(t))

    plt.plot(t, y)
    plt.xlabel('time (t)')
    plt.ylabel('value (y)')
    plt.title('Szum gaussowski')
    plt.grid(True)
    plt.show()
