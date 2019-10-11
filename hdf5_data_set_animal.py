import glob
import os.path as opath
import numpy as np
import pandas as pd
import h5py


'''
This is for generating hdf5 data set from npy files. 
-- f_ path: path to your data
-- animal: It is not important. Because I have separate data file folder for each experiment, I made 'animal' variable
        to indicate the folder path additionally. you can just delete it if you don't need
-- protocol_n: Similar to 'animal', this is the variable to store the name of the each folder for different experiment
               conditions. Also, if you don't need to have sub-sub folder path, you can remove it.
--- npy_f: Because each experiment condition data has several data files, I assigned this variable to all the files
           in an experiment condition folder and use len(npy_f) to generate arrays in hdf5 file
-- n_ch: the number of channels. Because I use 16 channel shank electrode probe, my data has 16 arrays for each data
         file. Therefore, I assigned n_ch to represent the number of arrays to generate hdf5 dataset array. If you
         use a different number of channels, change this value.
-- npy_name: This list is to store the name of the npy files so that I can check the order of the arrays in the dataset.                   
-- If there is 'l' at the end of a variable name, it is for LFP data. If there is 't' at the end of a variable name,
   it is for Tsp data. Again, also, you can change these settings whatever you like to fit in your situation.
-- Example of path to one experiment condition data file
   : '/home/bhc/OneDrive/Work/PhD/zwicker_tone/data/cr29_190228/strf/*.npy
-- ch_order: Because the recording system changed the order of ch 16 and ch 15, using ch_order, the array order should
             be changed.
'''

f_path = '/home/bhc/OneDrive/Work/PhD/zwicker_tone/data/'
animal = 'cr37_190408'
# aniaml list: cr29_190228, cr31_190312, cr32_190319, cr33_190321, cr35_190403, cr37_190408, cr43_190618, cr50_190724
protocol_n = [
              'strf', 'strf_1', 'strf_2', 'strf_3', 'strf_4', 'strf_5', 'strf_6', 'nnm_3_0', 'nnm_3_0_05', 'nnm_3_1',
              'nnm_1_1', 'nn_3_1', 'nn_1_1', 'nn_3_0', 'nnm_lef', 'nnm_hef', 'nn_wn_11', 'nn_wn_31', 'nn_wn_30',
              'nnm_wn', 'sil', 'tc'
             ]


ch_order = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 14])
n_ch = 16
npy_name_l = []
npy_name_t = []
dt = h5py.special_dtype(vlen=np.dtype('float32'))
arrays = []

'''LFP'''

with h5py.File(f_path + animal + '/' + animal + '_lfp.hdf5', 'w') as h_5:
    for p_n in protocol_n:
        npy_f = sorted(glob.glob(opath.join(f_path + animal + '/lfp/' + p_n, '*.npy')))
        npy_name_l.append(npy_f)
        h_5.create_dataset(p_n, (len(npy_f), n_ch), dtype=dt)

    for i in range(len(protocol_n)):
        npy_f = npy_name_l[i]

        for j in range(len(npy_f)):
            session_file = np.load(npy_f[j], allow_pickle=True)
            '''
             this k loop is here because when you load npy file converted from mat file, it stores elements like
             [[1], [2], [3],...], not [1, 2, 3, ...]. Therefore, you need to concatenate them to make one array.
            '''
            for k in range(n_ch):
                arrays.append(np.concatenate(session_file[ch_order[k]]))

            h_5[protocol_n[i]][j] = arrays
            arrays = []
            print(npy_f[j] + ' is done')


pd.DataFrame(npy_name_l).to_csv(f_path + animal + '/' + animal + '_lfp_list.csv')

'''Tsp'''

with h5py.File(f_path + animal + '/' + animal + '_tsp.hdf5', 'w') as h_5:
    for p_n in protocol_n:
        npy_f = sorted(glob.glob(opath.join(f_path + animal + '/tsp/' + p_n, '*.npy')))
        npy_name_t.append(npy_f)
        h_5.create_dataset(p_n, (len(npy_f), n_ch), dtype=dt)

    for i in range(len(protocol_n)):
        npy_f = npy_name_t[i]

        for j in range(len(npy_f)):
            session_file = np.load(npy_f[j], allow_pickle=True)
            '''
             this k loop is here because when you load npy file converted from mat file, it stores elements like
             [[0], [1], [2],...], not [0, 1, 2, ...]. Therefore, you need to concatenate them to make one array.
            '''
            for k in range(n_ch):
                arrays.append(np.concatenate(session_file[ch_order[k]]))

            h_5[protocol_n[i]][j] = arrays
            arrays = []
            print(npy_f[j] + ' is done')

pd.DataFrame(npy_name_t).to_csv(f_path + animal + '/' + animal + '_tsp_list.csv')
