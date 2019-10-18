import glob
import os.path as opath
import scipy.io as spio
import numpy as np


f_path = '/home/bhc/OneDrive/Work/PhD/zwicker_tone/data/'
animal = 'cr50_190724'
# aniaml list: cr29_190228, cr31_190312, cr32_190319, cr33_190321, cr35_190403, cr37_190408, cr43_190618, cr50_190724
protocol_n = [
               'strf_1', 'strf_2', 'strf_3', 'strf_4', 'strf_5', 'strf_6', 'nnm_3_0', 'nnm_3_0_60',
               'nnm_3_0_50', 'nnm_3_0_05', 'nnm_3_1', 'nnm_1_1', 'nn_3_1', 'nn_1_1', 'nn_3_0', 'nnm_lef', 'nnm_hef',
               'nn_wn_1_1', 'nn_wn_3_1', 'nnm_wn_3_0', 'nnm_wn_3_1', 'nnm_wn_1_1', 'tc', 'sil'
             ]

files_l = []
files_t = []

'''
lfp
'''

for i_file in protocol_n:
    d_path = glob.glob(opath.join(f_path + animal + '/lfp/' + i_file, '*.mat'))
    files_l.append(d_path)

# p_n = num of the protocols/ p_e = num of the sessions in one protocol
for p_n in range(len(files_l)):
    for p_e in range(len(files_l[p_n])):
        file_l = files_l[p_n][p_e]
        data = spio.loadmat(file_l)['LFP'][0]
        o_file = file_l.replace('mat', 'npy')
        print(o_file)
        np.save(o_file, data)

'''
This is to store mat files into Python dict. in testing['type of the data e.g. strf'],
it stores the whole data from different session/mat file.
- In testing['type'][#], it stores the data from one specific session/mat file.
- In testing['type'][#][#], it is this one matlab cell array section which shows  all the frequency arrays
- In testing['type'][#][#][#], you choose the data from one specific frequency.
- testing is a just the name of the dict to store the data. You can change it to whatever name you want e.g. lfp, tsp
Choose wisely to process them for the analysis.
'''

'''
tsp
'''

for i_file in protocol_n:
    d_path = glob.glob(opath.join(f_path + animal + '/tsp/' + i_file, '*.mat'))
    files_t.append(d_path)

# p_n = num of the protocols/ p_e = num of the sessions in one protocol
for p_n in range(len(files_t)):
    for p_e in range(len(files_t[p_n])):
        file_l = files_t[p_n][p_e]
        data = spio.loadmat(file_l)['Tsp'][0]
        o_file = file_l.replace('mat', 'npy')
        print(o_file)
        np.save(o_file, data)
