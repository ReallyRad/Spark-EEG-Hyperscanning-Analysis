import mne
import os
import numpy as np
import matplotlib.pyplot as plt

mne.set_log_level("WARNING")
raw = mne.io.read_raw_edf("PC2.edf", preload=True)
raw.rename_channels(lambda s: s.strip("."))
#raw.set_montage("standard_1020", match_case=False)
raw.set_eeg_reference("average")

n_time_samps = raw.n_times
time_secs = raw.times
ch_names = raw.ch_names
n_chan = len(ch_names)  # note: there is no raw.n_channels attribute
print('the (cropped) sample data object has {} time samples and {} channels.'
      ''.format(n_time_samps, n_chan))
print('The last time sample is at {} seconds.'.format(time_secs[-1]))
print('The first few channel names are {}.'.format(', '.join(ch_names[:3])))
print()  # insert a blank line in the output

# some examples of raw.info:
print('bad channels:', raw.info['bads'])  # chs marked "bad" during acquisition
print(raw.info['sfreq'], 'Hz')            # sampling frequency
print(raw.info['description'], '\n')      # miscellaneous acquisition info

print(raw.info)

sampling_freq = raw.info['sfreq']
start_end_secs = np.array([0, 43])
start_sample, stop_sample = (start_end_secs * sampling_freq).astype(int)

channel_names = ['Fp1', 'Audio']
two_meg_chans = raw[channel_names, start_sample:stop_sample]
y_offset = np.array([5e-11, 0])  # just enough to separate the channel traces
x = two_meg_chans[1]
y = two_meg_chans[0].T + y_offset
lines = plt.plot(x, y)
plt.legend(lines, channel_names)
plt.show()