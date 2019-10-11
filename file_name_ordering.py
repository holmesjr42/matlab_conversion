import glob
import os.path as opath
import scipy.io as spio
import numpy as np
import os

f_path = '/home/bhc/OneDrive/Work/PhD/zwicker_tone/data/'
animal = 'cr50_190724'
'''
aniaml list: cr29_190228, cr30_190305, cr31_190312, cr32_190319,
               cr33_190321, cr35_190403, cr37_190408, cr43_190618, cr50_190724
               
protocol = [
               'strf_1', 'strf_2', 'strf_3', 'strf_4', 'strf_5', 'strf_6', 'nnm_3_0', 'nnm_3_0_60',
               'nnm_3_0_50', 'nnm_3_0_05', 'nnm_3_1', 'nnm_1_1', 'nn_3_1', 'nn_1_1', 'nn_3_0', 'nnm_lef', 'nnm_hef',
               'nn_wn_1_1', 'nn_wn_3_1', 'nnm_wn_3_0', 'nnm_wn_3_1', 'nnm_wn_1_1', 'tc', 'sil'
             ]
'''
protocol_strf = [
               'strf_1', 'strf_2', 'strf_3', 'strf_4', 'strf_5', 'strf_6'
]

protocol_nnm = [
               'nnm_3_0', 'nnm_3_0_60', 'nnm_3_0_50', 'nnm_3_0_05', 'nnm_3_1', 'nnm_1_1', 'nnm_lef', 'nnm_hef',
               'nnm_wn_3_0', 'nnm_wn_3_1', 'nnm_wn_1_1'
             ]

protocol_nn = [
               'nn_3_1', 'nn_1_1', 'nn_wn_1_1', 'nn_wn_3_1'
              ]

protocol_tc = [
                'tc'
             ]

protocol_sil = [
                'sil'
             ]

files_strf_l = []
files_nnm_l = []
files_nn_l = []
files_tc_l = []
files_sil_l = []

files_strf_t = []
files_nnm_t = []
files_nn_t = []
files_tc_t = []
files_sil_t = []


coor_1 = len(f_path) + len(animal) + 5
# 5 = num of '/lfp/ or'/tsp/' and missing '/' from animal variable in file path


'''
nnm
'''
paths = ['/lfp/', '/tsp/']
for i_file in protocol_nnm:
    d_path_l = glob.glob(opath.join(f_path + animal + paths[0] + i_file))
    d_path_t = glob.glob(opath.join(f_path + animal + paths[1] + i_file))
    files_nnm_l.append(d_path_l)
    files_nnm_t.append(d_path_t)

files_nnm_l = np.concatenate(files_nnm_l)
files_nnm_t = np.concatenate(files_nnm_t)

# p_n = file_name

# lfp

for i in range(len(files_nnm_l)):
    for p_n in os.listdir(files_nnm_l[i]):
        if p_n[-6:-4] == '70':
            os.rename(opath.join(files_nnm_l[i] + '/' + p_n),
                      opath.join(files_nnm_l[i] + '/' + p_n.replace('LFP', '01_lfp')))
        elif p_n[-6:-4] == '60':
            os.rename(opath.join(files_nnm_l[i] + '/' + p_n),
                      opath.join(files_nnm_l[i] + '/' + p_n.replace('LFP', '02_lfp')))
        elif p_n[-6:-4] == '50':
            os.rename(opath.join(files_nnm_l[i] + '/' + p_n),
                      opath.join(files_nnm_l[i] + '/' + p_n.replace('LFP', '03_lfp')))
        elif p_n[-6:-4] == '40':
            os.rename(opath.join(files_nnm_l[i] + '/' + p_n),
                      opath.join(files_nnm_l[i] + '/' + p_n.replace('LFP', '04_lfp')))
        elif p_n[-6:-4] == '30':
            os.rename(opath.join(files_nnm_l[i] + '/' + p_n),
                      opath.join(files_nnm_l[i] + '/' + p_n.replace('LFP', '05_lfp')))
        else:
            print('nothing to change')

# tsp

    for p_n in os.listdir(files_nnm_t[i]):
        if p_n[-6:-4] == '70':
            os.rename(opath.join(files_nnm_t[i] + '/' + p_n),
                      opath.join(files_nnm_t[i] + '/' + p_n.replace('Tsp', '01_tsp')))
        elif p_n[-6:-4] == '60':
            os.rename(opath.join(files_nnm_t[i] + '/' + p_n),
                      opath.join(files_nnm_t[i] + '/' + p_n.replace('Tsp', '02_tsp')))
        elif p_n[-6:-4] == '50':
            os.rename(opath.join(files_nnm_t[i] + '/' + p_n),
                      opath.join(files_nnm_t[i] + '/' + p_n.replace('Tsp', '03_tsp')))
        elif p_n[-6:-4] == '40':
            os.rename(opath.join(files_nnm_t[i] + '/' + p_n),
                      opath.join(files_nnm_t[i] + '/' + p_n.replace('Tsp', '04_tsp')))
        elif p_n[-6:-4] == '30':
            os.rename(opath.join(files_nnm_t[i] + '/' + p_n),
                      opath.join(files_nnm_t[i] + '/' + p_n.replace('Tsp', '05_tsp')))
        else:
            print('nothing to change')



'''
nn
'''
for i_file in protocol_nn:
    d_path_l = glob.glob(opath.join(f_path + animal + paths[0] + i_file))
    files_nn_l.append(d_path_l)
    d_path_t = glob.glob(opath.join(f_path + animal + paths[1] + i_file))
    files_nn_t.append(d_path_t)

files_nn_l = np.concatenate(files_nn_l)
files_nn_t = np.concatenate(files_nn_t)

# p_n = file_name

# lfp

for i in range(len(files_nn_l)):
    # for p_n in os.listdir(files_nn_l[i]):
    #     if p_n[-17:-15] == '70':
    #         os.rename(opath.join(files_nn_l[i] + '/' + p_n),
    #                   opath.join(files_nn_l[i] + '/' + p_n.replace('LFP', '01_lfp')))
    #     elif p_n[-17:-15] == '60':
    #         os.rename(opath.join(files_nn_l[i] + '/' + p_n),
    #                   opath.join(files_nn_l[i] + '/' + p_n.replace('LFP', '02_lfp')))
    #     else:
    #         print('nothing to change')

# tsp

    for p_n in os.listdir(files_nn_t[i]):
        if p_n[-17:-15] == '70':
            os.rename(opath.join(files_nn_t[i] + '/' + p_n),
                      opath.join(files_nn_t[i] + '/' + p_n.replace('Tsp', '01_tsp')))
        elif p_n[-17:-15] == '60':
            os.rename(opath.join(files_nn_t[i] + '/' + p_n),
                      opath.join(files_nn_t[i] + '/' + p_n.replace('Tsp', '02_tsp')))
        else:
            print('nothing to change')

'''
strf
'''
for i_file in protocol_strf:
    d_path_l = glob.glob(opath.join(f_path + animal + paths[0] + i_file))
    files_strf_l.append(d_path_l)
    d_path_t = glob.glob(opath.join(f_path + animal + paths[1] + i_file))
    files_strf_t.append(d_path_t)

files_strf_l = np.concatenate(files_strf_l)
files_strf_t = np.concatenate(files_strf_t)

# p_n = file_name

# lfp

for i in range(len(files_strf_l)):
    for p_n in os.listdir(files_strf_l[i]):
        if p_n[-18:-16] == '70':
            os.rename(opath.join(files_strf_l[i] + '/' + p_n),
                      opath.join(files_strf_l[i] + '/' + p_n.replace('LFP', '01_lfp')))
        elif p_n[-18:-16] == '60':
            os.rename(opath.join(files_strf_l[i] + '/' + p_n),
                      opath.join(files_strf_l[i] + '/' + p_n.replace('LFP', '02_lfp')))
        elif p_n[-18:-16] == '50':
            os.rename(opath.join(files_strf_l[i] + '/' + p_n),
                      opath.join(files_strf_l[i] + '/' + p_n.replace('LFP', '03_lfp')))
        elif p_n[-18:-16] == '40':
            os.rename(opath.join(files_strf_l[i] + '/' + p_n),
                      opath.join(files_strf_l[i] + '/' + p_n.replace('LFP', '04_lfp')))
        elif p_n[-18:-16] == '30':
            os.rename(opath.join(files_strf_l[i] + '/' + p_n),
                      opath.join(files_strf_l[i] + '/' + p_n.replace('LFP', '05_lfp')))
        else:
            print('nothing to change')

# tsp

    for p_n in os.listdir(files_strf_t[i]):
        if p_n[-18:-16] == '70':
            os.rename(opath.join(files_strf_t[i] + '/' + p_n),
                      opath.join(files_strf_t[i] + '/' + p_n.replace('Tsp', '01_tsp')))
        elif p_n[-18:-16] == '60':
            os.rename(opath.join(files_strf_t[i] + '/' + p_n),
                      opath.join(files_strf_t[i] + '/' + p_n.replace('Tsp', '02_tsp')))
        elif p_n[-18:-16] == '50':
            os.rename(opath.join(files_strf_t[i] + '/' + p_n),
                      opath.join(files_strf_t[i] + '/' + p_n.replace('Tsp', '03_tsp')))
        elif p_n[-18:-16] == '40':
            os.rename(opath.join(files_strf_t[i] + '/' + p_n),
                      opath.join(files_strf_t[i] + '/' + p_n.replace('Tsp', '04_tsp')))
        elif p_n[-18:-16] == '30':
            os.rename(opath.join(files_strf_t[i] + '/' + p_n),
                      opath.join(files_strf_t[i] + '/' + p_n.replace('Tsp', '05_tsp')))
        else:
            print('nothing to change')







'''
tc
'''
for i_file in protocol_tc:
    d_path_l = glob.glob(opath.join(f_path + animal + paths[0] + i_file))
    files_tc_l.append(d_path_l)
    d_path_t = glob.glob(opath.join(f_path + animal + paths[1] + i_file))
    files_tc_t.append(d_path_t)

files_tc_l = np.concatenate(files_tc_l)
files_tc_t = np.concatenate(files_tc_t)

# p_n = file_name

#lfp

for i in range(len(files_tc_l)):
    for p_n in os.listdir(files_tc_l[i]):
        tcs = p_n.split('-')
        numb_1 = str(tcs[3])
        numb_2 = numb_1.zfill(3)
        os.rename(opath.join(
                             files_tc_l[i] + '/' + tcs[0] + '-' + tcs[1] + '-' + tcs[2] + '-' +
                             tcs[3] + '-' + tcs[4]
                            ),
                  opath.join(
                             files_tc_l[i] + '/' + tcs[0] + '-' + tcs[1] + '-' + tcs[2] + '-' +
                             tcs[3].replace(str(numb_1), str(numb_2)) + '-' + tcs[4]
                            )
                  )

# tsp

    for p_n in os.listdir(files_tc_t[i]):
        tcs = p_n.split('-')
        numb_1 = str(tcs[3])
        numb_2 = numb_1.zfill(3)
        os.rename(opath.join(
                             files_tc_t[i] + '/' + tcs[0] + '-' + tcs[1] + '-' + tcs[2] + '-' +
                             tcs[3] + '-' + tcs[4]
                            ),
                  opath.join(
                             files_tc_t[i] + '/' + tcs[0] + '-' + tcs[1] + '-' + tcs[2] + '-' +
                             tcs[3].replace(str(numb_1), str(numb_2)) + '-' + tcs[4]
                            )
                  )

'''
sil
'''
for i_file in protocol_sil:
    d_path_l = glob.glob(opath.join(f_path + animal + paths[0] + i_file))
    files_sil_l.append(d_path_l)
    d_path_t = glob.glob(opath.join(f_path + animal + paths[1] + i_file))
    files_sil_t.append(d_path_t)

files_sil_l = np.concatenate(files_sil_l)
files_sil_t = np.concatenate(files_sil_t)

# # p_n = file_name

# lfp

for i in range(len(files_sil_l)):
    for p_n in os.listdir(files_sil_l[i]):
        tcs = p_n.split('-')
        numb_1 = str(tcs[3])
        numb_2 = numb_1.zfill(3)
        os.rename(opath.join(
                             files_sil_l[i] + '/' + tcs[0] + '-' + tcs[1] + '-' + tcs[2] + '-' +
                             tcs[3] + '-' + tcs[4]
                            ),
                  opath.join(
                             files_sil_l[i] + '/' + tcs[0] + '-' + tcs[1] + '-' + tcs[2] + '-' +
                             tcs[3].replace(str(numb_1), str(numb_2)) + '-' + tcs[4]
                            )
                  )

# tsp

    for p_n in os.listdir(files_sil_t[i]):
        tcs = p_n.split('-')
        numb_1 = str(tcs[3])
        numb_2 = numb_1.zfill(3)
        os.rename(opath.join(
                             files_sil_t[i] + '/' + tcs[0] + '-' + tcs[1] + '-' + tcs[2] + '-' +
                             tcs[3] + '-' + tcs[4]
                            ),
                  opath.join(
                             files_sil_t[i] + '/' + tcs[0] + '-' + tcs[1] + '-' + tcs[2] + '-' +
                             tcs[3].replace(str(numb_1), str(numb_2)) + '-' + tcs[4]
                            )
                  )



