import pickle


def serialize_signal(sig, filename):
    bin_file = open('bin/' + filename + '.bin', mode='wb')
    pickle.dump(sig, bin_file)
    bin_file.close()


def deserialize_signal(filename):
    bin_file = open('bin/' + filename + '.bin', mode='rb')
    sig = pickle.load(bin_file)
    bin_file.close()

    return sig
