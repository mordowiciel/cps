class CPSSignal:
    t0 = 0
    sampling_freq = 1
    values = []
    name = ""
    discret = False

    def __init__(self, name, t0, t1, sampling_freq, values, discret=False):
        self.t0 = t0
        self.t1 = t1
        self.sampling_freq = sampling_freq
        self.values = values
        self.name = name
        self.discret = discret
