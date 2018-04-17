import numpy as np
import plot_utils
from cpssignal import *


# TODO : zakladamy, ze sygnaly maja identyczny przedzial czasowy oraz okres probkowania -> wprowadzic walidacje!

def add_signals(sig1, sig2):
    values_sum = np.add(sig1.values, sig2.values)
    name = sig1.name + " + " + sig2.name
    new_sig = CPSSignal(name, sig1.t0, sig1.t1, sig1.sampling_freq, values_sum)
    return new_sig


def substract_signals(sig1, sig2):
    values_sub = np.subtract(sig1.values, sig2.values)
    name = sig1.name + " - " + sig2.name

    new_sig = CPSSignal(name, sig1.t0, sig1.t1, sig1.sampling_freq, values_sub)
    return new_sig


def multiply_signals(sig1, sig2):
    values_mul = np.multiply(sig1.values, sig2.values)
    name = sig1.name + " * " + sig2.name
    new_sig = CPSSignal(name, sig1.t0, sig1.t1, sig1.sampling_freq, values_mul)
    return new_sig


def divide_signals(sig1, sig2):
    values_div = np.divide(sig1.values, sig2.values)
    name = sig1.name + " / " + sig2.name
    new_sig = CPSSignal(name, sig1.t0, sig1.t1, sig1.sampling_freq, values_div)
    return new_sig
