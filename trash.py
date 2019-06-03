import glob
import os.path as opath
import numpy as np
import pandas as pd
import h5py

f_path = '/home/bhc/OneDrive/Work/PhD/zwicker_tone/data/'
animal = 'cr29_190228'
protocol_n = [
           'strf', 'nnm_3_0', 'nm_3_0_05', 'nnm_3_1', 'nnm_1_1', 'nn_3_1', 'nn_1_1', 'nnm_lef',
           'nnm_hef', 'nnm_wn', 'nn_wn', 'sil', 'tc'
]


with h5py.File(f_path + animal + '/cr29_190228_lfp.hdf5', 'r') as h_5:
    print(h_5['strf'][0][15])
