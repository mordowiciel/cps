import numpy as np
import utils


def szum_jednostajny(A, t1, d):
    t = np.arange(t1, t1 + d, 0.01)
    y = np.random.uniform(-A, A, len(t))

    utils.plot_signal(t, y, 'Uniform noise')

    return y


def szum_gaussowski(A, t1, d):
    t = np.arange(t1, t1 + d, 0.01)
    y = np.random.normal(-A, A, len(t))

    utils.plot_signal(t, y, 'Gaussian noise')

    return y
