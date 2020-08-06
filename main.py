import mne
import numpy as np
import matplotlib.pyplot as plt

mne.set_log_level("WARNING")
raw = mne.io.read_raw_edf("PC1.edf", preload=True)

chs = ['Audio']
chan_idx = [raw.ch_names.index(ch) for ch in chs]

raw.plot(order = chan_idx)

x = 3