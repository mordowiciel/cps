import numpy as np
import scipy.stats as stats
from cpssignal import CPSSignal


def uniform(A, t1, d, sampling_freq):
    sampling_step = 1.0 / sampling_freq

    t = np.arange(t1, t1 + d, sampling_step)
    y = np.random.uniform(-A, A, len(t))

    return CPSSignal(t1, t1 + d, sampling_freq, y)


def gaussian(A, t1, d, sampling_freq):
    sampling_step = 1.0 / sampling_freq

    t = np.arange(t1, t1 + d, sampling_step)
    truncated_gaussian_generator = truncated_normal(low=-A, upp=A)
    y = truncated_gaussian_generator.rvs(len(t))

    return CPSSignal(t1, t1 + d, sampling_freq, y)


# Helper function to generate Gaussian distribution within given range
def truncated_normal(mean=0, sd=1, low=0, upp=10):
    return stats.truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)
