import matplotlib.pyplot as plt
import numpy as np


def szum_jednostajny(A, t1, d):
    t = np.arange(t1, t1 + d, 0.01)
    y = np.random.uniform(-A, A, len(t))

    plt.plot(t, y)
    plt.xlabel('time (t)')
    plt.ylabel('value (y)')
    plt.title('Szum jednostajny')
    plt.grid(True)
    plt.show()

    return y


def szum_gaussowski(A, t1, d):
    t = np.arange(t1, t1 + d, 0.01)
    y = np.random.normal(-A, A, len(t))

    plt.plot(t, y)
    plt.xlabel('time (t)')
    plt.ylabel('value (y)')
    plt.title('Szum gaussowski')
    plt.grid(True)
    plt.show()

    return y
