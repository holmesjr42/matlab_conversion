import glob
import os.path as opath
import numpy as np
import pandas as pd
import h5py
import os
import pickle
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

animal = animals[5]
'''
for one animal
'''
# hdf5 file
# for animal in animals:
protocol_n = os.listdir(f_path + animal + '/tsp/')
protocol_n.remove('other')
matool.to_hdf5(path=f_path, animal=animal, protocol=protocol_n)

# file name dictionary

hey = matool.names(path=f_path, animal=animal, protocol=protocol_n)

with open(f_path + '/' + animal + '/' + animal[0:5] + 'names_lfp.pk',
          'wb') as naml:
    pickle.dump(hey[1], naml, protocol=pickle.HIGHEST_PROTOCOL)

with open(f_path + '/' + animal + '/' + animal[0:5] + 'names_tsp.pk',
          'wb') as namt:
    pickle.dump(hey[0], namt, protocol=pickle.HIGHEST_PROTOCOL)
