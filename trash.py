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
 do not erase this
'''
# convert time index
# sr = 97656.25
# file = '/home/bhc/codes/sth_matlab' \
#        '/time_index_multi_tones_500ms_180sec_nn_3_1.mat'
# file2 = '/home/bhc/codes/sth_matlab' \
#         '/time_index_multi_tones_500ms_180sec_nn_1_1.mat'
#
# time_index = spio.loadmat(file)['time_index_nn_3_1']
# time_index2 = spio.loadmat(file2)['time_index_nn_1_1']
#
# t_index = {'t_index_31_nn': [], 't_index_31_si': [], 't_index_11_nn': [],
#            't_index_11_si': []}
#
# group = list(t_index.keys())
#
# for i in range(len(time_index)):
#     for j in range(len(time_index[i])):
#         t_index[group[i]].append(np.concatenate(time_index[i][j]))
#         t_index[group[i+2]].append(np.concatenate(time_index2[i][j]))
#
#
# # for i in range(len(time_index)):
# #     time_index[i] = time_index[i]/sr*1000
#
# with open('/home/bhc/codes/spikes_classics/parameters'
#           '/time_index_multi_tones_500ms_180s_nn_si.pk', 'wb') as ofile:
#     pickle.dump(t_index, ofile, protocol=pickle.HIGHEST_PROTOCOL)
# ofile = '/home/bhc/codes/spikes_classics/time_index_multi_tones_500ms_180s.npy'
# np.save(ofile, time_index)
# data = np.load(ofile, allow_pickle=True)
# print(data[0])
# file_l = '/home/bhc/Documents/test/MUA_07-Aug-2019-20-TC_500_32000_0.125_70_10.mat'
# data = spio.loadmat(file_l)['MUA'][0][12]

# for i in range(16):
#     data2.append(np.concatenate(data[i]))
#     print('channel', i, 'finished')
# print(data2[1].dtype)
# # print(data2[1])
# o_file = file_l.replace('mat', 'npy')
# print(data.dtype, np.shape(data))
# print(o_file)
# np.save(o_file, data)

with open('/home/bhc/codes/spikes_classics/parameters'
          '/time_index_multi_tones_500ms_180s_nn_si.pk', 'rb') as ofile:
    r = pickle.load(ofile)