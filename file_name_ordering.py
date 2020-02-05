import glob
import os.path as opath
import numpy as np
import os
import fname_tools as ft

f_path = '/home/bhc/OneDrive/Work/PhD/projects/zwicker_tone_2018_2021/data/'
animal = 'cr50_190724'
'''
aniaml list
 
 Zwicker tone:  cr29_190228, cr30_190305, cr31_190312, cr33_190321, 
                cr35_190403, cr50_190724
               
 GABAZine
 
Protocols
 
 Zwicker tone: strf, nnm, nn, tc, sil
 
 GABAzine: strf, tc, sil
               
'''

protocols = os.listdir(f_path+animal+'/tsp/')

protocol_strf = [p for p in protocols if "strf_" in p]
protocol_nnm = [p for p in protocols if "nnm_" in p]
protocol_nn = [p for p in protocols if "nn_" in p]
protocol_tc = [p for p in protocols if "tc" in p]
protocol_sil = [p for p in protocols if "sil" in p]


coor_1 = len(f_path) + len(animal) + 5

# 5 = num of '/lfp/ or'/tsp/' and
# missing '/' from animal variable in file path

paths = ['/lfp/', '/tsp/']

'''
GABAZine
'''
# ft.strf_o(prot=protocol_strf, path_1=f_path, path_2=paths, animal=animal)
# ft.tcg_o(prot=protocol_tc, path_1=f_path, path_2=paths, animal=animal)
# ft.sil_o(prot=protocol_sil, path_1=f_path, path_2=paths, animal=animal)

'''
Zwicker tone
'''
ft.strf_o(prot=protocol_strf, path_1=f_path, path_2=paths, animal=animal)
ft.nnm_o(prot=protocol_nnm, path_1=f_path, path_2=paths, animal=animal)
ft.nn_o(prot=protocol_nn, path_1=f_path, path_2=paths, animal=animal)
ft.tc_o(prot=protocol_tc, path_1=f_path, path_2=paths, animal=animal)
ft.sil_o(prot=protocol_sil, path_1=f_path, path_2=paths, animal=animal)
