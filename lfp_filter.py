import mat_conv_tools as matool
import numpy as np
import h5py

'''
sr, sampling rate; f1, f2, min max of the band range you are going to 
filter out. In this case, I'll remove 50 kHz noise with band range 49 -- 51 Hz
'''
sr = 1061.5
f1 = 49
f2 = 51

# to make a new data set for the filtered signal
dt = h5py.special_dtype(vlen=np.dtype('float32'))
arrays = []
n_ch = 16

# paths and keys for the data set
f_path = '/home/bhc/OneDrive/Work/PhD/projects/zwicker_tone_2018_2021/data/'
animal = 'cr50_190724'

# aniaml list: cr29_190228, cr30_190228, cr31_190312, cr33_190321, cr35_190403,
# 			   cr50_190724

with h5py.File(f_path + animal + '/' + animal + '_lfp.hdf5', 'r') as h_5:
    protocol_n = list(h_5.keys())
    with h5py.File(f_path + animal + '/' + animal + '_lfp_fil.hdf5', 'w') as h_f:
        # creating the data set for the filtered lfp
        for i in protocol_n:
            h_f.create_dataset(i, (len(h_5[i]), n_ch), dtype=dt)
        # filtering lfp
        for i in protocol_n:
            for j in range(len(h_5[i])):
                for k in range(len(h_5[i][j])):
                    filtered = matool.fft_filter(h_5[i][j][k], sr, f1, f2)
                    arrays.append(filtered)
                h_f[i][j] = arrays
                arrays = []
            print(i + ' is done')
