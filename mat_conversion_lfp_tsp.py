import glob
import os.path as opath
import scipy.io as spio
import numpy as np
import os
import mat_conv_tools as matool

f_path = '/home/bhc/OneDrive/Work/PhD/projects/zwicker_tone_2018_2021/data/'
animal = 'cr50_190724'
# aniaml list: cr29_190228, cr30_190228, cr31_190312, cr33_190321, cr35_190403,
# 			   cr50_190724

animals = ['cr29_190228', 'cr30_190305', 'cr31_190312', 'cr33_190321',
           'cr35_190403', 'cr50_190724']

for a in animals:
	protocol_n = os.listdir(f_path + a + '/tsp/')
	matool.mat_npy(animal=a, protocol=protocol_n, path=f_path)
	print(a, ' is finished')
