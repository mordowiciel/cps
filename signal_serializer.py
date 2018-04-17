import pickle
import os


def serialize_signal(sig, filename):
    if not os.path.exists('bin/'):
        os.makedirs('bin/')

    bin_file = open('bin/' + filename + '.bin', mode='wb')
    pickle.dump(sig, bin_file)
    bin_file.close()


def deserialize_signals():
    path = 'bin/'
    signals = []
    for filename in os.listdir(path):
        bin_file = open('bin/' + filename, mode='rb')
        sig = pickle.load(bin_file)
        signals.append(sig)
        bin_file.close()
    return signals
