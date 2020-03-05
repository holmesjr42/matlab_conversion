import glob
import os.path as opath
import numpy as np
import pandas as pd
import h5py
import scipy.io as spio
import os
import mat_conv_tools as matool
import pickle
# f_path = '/home/bhc/OneDrive/Work/PhD/projects/gabazine_2019_2020/data/'
# animal = 'cr60_190924'
#
# protocol_strf = []
# # protocol_nnm = []
# protocol_nn = []
# protocol_tc = []
# protocol_sil = []
#
# protocols = os.listdir(f_path+animal+'/tsp/')
#
# protocol_nnm = [p for p in protocols if "tc" in p]
#
# print(protocol_nnm, protocols)
# protocol_n = [
#            'strf', 'nnm_3_0', 'nm_3_0_05', 'nnm_3_1', 'nnm_1_1', 'nn_3_1', 'nn_1_1', 'nnm_lef',
#            'nnm_hef', 'nnm_wn', 'nn_wn', 'sil', 'tc'
# ]
#
#
# with h5py.File(f_path + animal + '/cr29_190228_lfp.hdf5', 'r') as h_5:
#     print(h_5['strf'][0][15])


# f_path = '/home/bhc/OneDrive/Work/PhD/zwicker_tone/data/'
# animal = 'cr35_190403'
#
# with h5py.File(f_path + animal + '/' + animal + '_lfp.hdf5', 'r') as h_5:
#         filtered = filt.fft_filter(h_5['nn_3_1'][1][0], 1061.5, 49, 51)
#         # print(h_5['nn_3_1'][1][0])
#         print(filtered)
#     # print(h_5['nn_3_1'][1][0])
'''
convert time index

# file = '/home/bhc/OneDrive/Work/PhD/zwicker_tone/data/code_matlab/time_index_multi_tones_500ms_180sec.mat'
# time_index = spio.loadmat(file)['time_index']
# time_index = np.concatenate(time_index)
#
# for i in range(len(time_index)):
#     time_index[i] = np.concatenate(time_index[i])
#
# for i in range(len(time_index)):
#     time_index[i] = time_index[i]/97656.25*1000
#
# ofile = '/home/bhc/codes/spikes_classics/time_index_multi_tones_500ms_180s.npy'
# # np.save(ofile, time_index)
# data = np.load(ofile, allow_pickle=True)
# print(data[0])
file_l = '/home/bhc/Documents/test/MUA_07-Aug-2019-20-TC_500_32000_0.125_70_10.mat'
data = spio.loadmat(file_l)['MUA'][0][12]

# for i in range(16):
#     data2.append(np.concatenate(data[i]))
#     print('channel', i, 'finished')
# print(data2[1].dtype)
# print(data2[1])
o_file = file_l.replace('mat', 'npy')
print(data.dtype, np.shape(data))
print(o_file)
np.save(o_file, data)
'''


