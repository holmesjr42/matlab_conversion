import glob
import numpy as np
import scipy.fftpack as ft
import os.path as opath
import scipy.io as spio
import glob
import pandas as pd
import h5py
import os
import pickle

'''
mat to npy

- animal: animal number and date. If you are not sure about what it is, 
       check the folder name in 
       OneDrive/Work/PhD/porjects/zwickertone_2019_2021

- protocol: protocol folder names in either 
		  OneDrive/Work/PhD/porjects/zwickertone_2019_2021/animal/tps or 
          OneDrive/Work/PhD/porjects/zwickertone_2019_2021/animal/lfp

- path: path to the animal name folder

This is to store mat files into Python dict. in testing['type of the data 
e.g. strf'],
it stores the whole data from different session/mat file.
- In testing['type'][#], it stores the data from one specific session/mat file.
- In testing['type'][#][#], it is this one matlab cell array section 
  which shows all the frequency arrays
- In testing['type'][#][#][#], you choose the data from one specific frequency.
- testing is a just the name of the dict to store the data. You can change it 
  to whatever name you want e.g. lfp, tsp
Choose wisely to process them for the analysis.

'''


def mat_npy(animal, protocol, path):
    for i_file in protocol:
        files_l = []
        files_t = []
        d_path = glob.glob(opath.join(path + animal + '/lfp/'
                                      + i_file, '*.mat'))
        files_l.append(d_path)

        d_path = glob.glob(opath.join(path + animal + '/tsp/'
                                      + i_file, '*.mat'))
        files_t.append(d_path)

        # lfp
        # p_n = num of the protocols/ p_e = num of the sessions in one protocol
        for p_n in range(len(files_l)):
            for p_e in range(len(files_l[p_n])):
                file_l = files_l[p_n][p_e]
                data = spio.loadmat(file_l)['LFP'][0]
                o_file = file_l.replace('mat', 'npy')
                # print(o_file)
                np.save(o_file, data)
        # tsp

        for p_n in range(len(files_t)):
            for p_e in range(len(files_t[p_n])):
                file_l = files_t[p_n][p_e]
                data = spio.loadmat(file_l)['Tsp'][0]
                o_file = file_l.replace('mat', 'npy')
                # print(o_file)
                np.save(o_file, data)


'''
fast fourier transform filter
'''

'''
s: signal, fe: sampling frequency, f1, f2: frequencies for band pass filter
'''


def fft_filter(s, fe, f1, f2):
    tf_s = ft.fft(s)
    n_samp = len(s)
    # frequency = fe*n/N(sample number)
    n1 = int(n_samp * f1 / fe)
    # was nsamp/2, nb are for the symmetrical parts left and right of nyquist f
    n1b = int(n_samp - n1)
    n2 = int(n_samp * f2 / fe)
    n2b = int(n_samp - n2)
    temp = tf_s
    temp[n1:n2] = 0
    temp[n2b:n1b] = 0
    itf_tf_s = ft.ifft(temp)
    return itf_tf_s


def to_hdf5(path, animal, protocol):

    npy_name_l = []
    npy_name_t = []
    n_ch = 16
    dt = h5py.special_dtype(vlen=np.dtype('float32'))
    ch_order = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 14])
    arrays = []

    '''lfp'''

    with h5py.File(path + animal + '/' + animal + '_lfp.hdf5', 'w') as h_5:
        for p_n in protocol:
            npy_f = sorted(glob.glob(opath.join(path + animal + '/lfp/'
                                                + p_n, '*.npy')))
            h_5.create_dataset(p_n, (len(npy_f), n_ch), dtype=dt)
            npy_name_l.append(npy_f)

        for i in range(len(protocol)):
            npy_f = npy_name_l[i]

            for j in range(len(npy_f)):
                session_file = np.load(npy_f[j], allow_pickle=True)
                '''
                 this k loop is here because when you load npy file converted
                 from mat file, it stores elements like [[1], [2], [3],...],
                 not [1, 2, 3, ...]. Therefore, you need to concatenate them
                 to make one array.
                '''
                for k in range(n_ch):
                    arrays.append(np.concatenate(session_file[ch_order[k]]))

                h_5[protocol[i]][j] = arrays
                arrays = []
                print(npy_f[j] + ' is done')

    pd.DataFrame(npy_name_l).to_csv(path + animal + '/' + animal +
                                    '_lfp_list.csv')

    '''tsp'''

    with h5py.File(path + animal + '/' + animal + '_tsp.hdf5', 'w') as h_5:
        for p_n in protocol:
            npy_f = sorted(glob.glob(opath.join(path + animal
                                                + '/tsp/' + p_n, '*.npy')))
            h_5.create_dataset(p_n, (len(npy_f), n_ch), dtype=dt)
            npy_name_t.append(npy_f)

        for i in range(len(protocol)):
            npy_f = npy_name_t[i]

            for j in range(len(npy_f)):
                session_file = np.load(npy_f[j], allow_pickle=True)
                '''
                 this k loop is here because when you load npy file converted from
                 mat file, it stores elements like [[0], [1], [2],...],
                 not [0, 1, 2, ...]. Therefore, you need to concatenate them
                 to make one array.
                '''
                for k in range(n_ch):
                    arrays.append(np.concatenate(session_file[ch_order[k]]))

                h_5[protocol[i]][j] = arrays
                arrays = []
                print(npy_f[j] + ' is done')

    pd.DataFrame(npy_name_t).to_csv(path + animal + '/' + animal +
                                    '_tsp_list.csv')

##################################################
def names(path, animal, protocol):

    npy_l = []
    npy_t = []
    names_t = {}
    names_l = {}
    for p_n in protocol:
        npy_f_t = sorted(glob.glob(opath.join(path + animal + '/tsp/' + p_n,
                                              '*.npy')))
        npy_f_l = sorted(glob.glob(opath.join(path + animal + '/lfp/' + p_n,
                                              '*.npy')))

        for i in range(len(npy_f_t)):

            if p_n[0:4] == 'nnm_':
                nme = npy_f_t[i].split('-')
                npy_t.append((p_n + '_' + 'zt' + nme[4][2:5] + '_' + nme[4][
                                                                     -11:-4]))
            elif p_n[0:3] == 'nn_':
                nme = npy_f_t[i].split('-')
                npy_t.append((p_n + '_' + nme[4][0:5]))

            elif p_n[0:4] == 'strf':
                nme = npy_f_t[i].split('-')
                npy_t.append((p_n + '_' + nme[4][3:5]))

            else:
                npy_t.append((npy_f_t[i]))

        for j in range(len(npy_f_l)):

            if p_n[0:4] == 'nnm_':
                nml = npy_f_l[j].split('-')
                npy_l.append((p_n + '_' + 'zt' + nml[4][2:5] + '_' + nml[4][
                                                                     -11:-4]))
            elif p_n[0:3] == 'nn_':
                nml = npy_f_l[j].split('-')
                npy_l.append((p_n + '_' + nml[4][0:5]))

            elif p_n[0:4] == 'strf':
                nml = npy_f_l[j].split('-')
                npy_l.append((p_n + '_' + nml[4][3:5]))

            else:
                npy_l.append((npy_f_l[j]))

        names_t[p_n] = npy_t
        names_l[p_n] = npy_l
        npy_t = []
        npy_l = []

    return [names_t, names_l]





