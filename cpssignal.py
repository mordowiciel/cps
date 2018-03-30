class CPSSignal:
    t0 = 0
    sampling_freq = 1
    values = []

    def __init__(self, t0, t1, sampling_freq, values):
        self.t0 = t0
        self.t1 = t1
        self.sampling_freq = sampling_freq
        self.values = values
