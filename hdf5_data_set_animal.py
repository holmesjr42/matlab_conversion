import glob
import os.path as opath
import numpy as np
import pandas as pd
import h5py
import os
import mat_conv_tools as matool
'''
This is for generating hdf5 data set from npy files. 
-- f_ path: path to your data

-- animal: It is not important. Because I have separate data file folder for 
           each experiment, I made 'animal' variable to indicate the folder 
           path additionally. you can just delete it if you don't need

-- protocol_n: Similar to 'animal', this is the variable to store the name of 
               the each folder for different experiment conditions. 
               Also, if you don't need to have sub-sub folder path, you can 
               remove it.

--- npy_f: Because each experiment condition data has several data files, 
           I assigned this variable to all the files in an experiment 
           condition folder and use len(npy_f) to generate arrays in hdf5 file.

-- n_ch: the number of channels. Because I use 16 ch shank electrode probe, 
         my data has 16 arrays for each data file. Therefore, I assigned 
         n_ch to represent the number of arrays to generate hdf5 dataset array.
         If you use a different number of channels, change this value.

-- npy_name: This list is to store the name of the npy files so that 
             I can check the order of the arrays in the dataset.                   

-- If there is 'l' at the end of a variable name, it is for lfp data. 
   If there is 't' at the end of a variable name,
   it is for tsp data. Again, also, you can change these settings
   whatever you like to fit in your situation.

-- Example of path to one experiment condition data file
   : '/home/bhc/OneDrive/Work/PhD/zwicker_tone/data/cr29_190228/strf/*.npy
-- ch_order: Because the recording system changed the order of ch 16 and ch 15, 
             using ch_order, the array order should be changed.
'''

f_path = '/home/bhc/OneDrive/Work/PhD/projects/zwicker_tone_2018_2021/data/'
animals = ['cr29_190228', 'cr30_190305', 'cr31_190312', 'cr33_190321',
           'cr35_190403', 'cr50_190724', 'cr79_200211']

animal = animals[0]
'''
for one animal
'''

protocol_n = os.listdir(f_path + animal + '/tsp/')
protocol_n.remove('other')
matool.to_hdf5(path=f_path, animal=animal, protocol=protocol_n)









# '''lfp'''
#
# with h5py.File(f_path + animal + '/' + animal + '_lfp.hdf5', 'w') as h_5:
#     for p_n in protocol_n:
#         npy_f = sorted(glob.glob(opath.join(f_path + animal + '/lfp/'
#                                             + p_n, '*.npy')))
#         npy_name_l.append(npy_f)
#         h_5.create_dataset(p_n, (len(npy_f), n_ch), dtype=dt)
#
#     for i in range(len(protocol_n)):
#         npy_f = npy_name_l[i]
#
#         for j in range(len(npy_f)):
#             session_file = np.load(npy_f[j], allow_pickle=True)
#             '''
#              this k loop is here because when you load npy file converted from
#              mat file, it stores elements like [[1], [2], [3],...],
#              not [1, 2, 3, ...]. Therefore, you need to concatenate them
#              to make one array.
#             '''
#             for k in range(n_ch):
#                 arrays.append(np.concatenate(session_file[ch_order[k]]))
#
#             h_5[protocol_n[i]][j] = arrays
#             arrays = []
#             print(npy_f[j] + ' is done')
#
#
# pd.DataFrame(npy_name_l).to_csv(f_path + animal + '/'
#                                 + animal + '_lfp_list.csv')
#
# '''tsp'''
#
# with h5py.File(f_path + animal + '/' + animal + '_tsp.hdf5', 'w') as h_5:
#     for p_n in protocol_n:
#         npy_f = sorted(glob.glob(opath.join(f_path + animal
#                                             + '/tsp/' + p_n, '*.npy')))
#         npy_name_t.append(npy_f)
#         h_5.create_dataset(p_n, (len(npy_f), n_ch), dtype=dt)
#
#     for i in range(len(protocol_n)):
#         npy_f = npy_name_t[i]
#
#         for j in range(len(npy_f)):
#             session_file = np.load(npy_f[j], allow_pickle=True)
#             '''
#              this k loop is here because when you load npy file converted from
#              mat file, it stores elements like [[0], [1], [2],...],
#              not [0, 1, 2, ...]. Therefore, you need to concatenate them
#              to make one array.
#             '''
#             for k in range(n_ch):
#                 arrays.append(np.concatenate(session_file[ch_order[k]]))
#
#             h_5[protocol_n[i]][j] = arrays
#             arrays = []
#             print(npy_f[j] + ' is done')
#
# pd.DataFrame(npy_name_t).to_csv(f_path + animal + '/'
#                                 + animal + '_tsp_list.csv')
