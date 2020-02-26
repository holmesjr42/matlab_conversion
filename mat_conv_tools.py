import glob
import numpy as np
import scipy.fftpack as ft
import os.path as opath
import scipy.io as spio

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
				print(o_file)
				np.save(o_file, data)
		# tsp

		for p_n in range(len(files_t)):
			for p_e in range(len(files_t[p_n])):
				file_l = files_t[p_n][p_e]
				data = spio.loadmat(file_l)['Tsp'][0]
				o_file = file_l.replace('mat', 'npy')
				print(o_file)
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
	n1 = int(n_samp * f1/fe)
	# was nsamp/2, nb are for the symmetrical parts left and right of nyquist f
	n1b = int(n_samp - n1)
	n2 = int(n_samp * f2/fe)
	n2b = int(n_samp - n2)
	temp = tf_s
	temp[n1:n2] = 0
	temp[n2b:n1b] = 0
	itf_tf_s = ft.ifft(temp)
	return itf_tf_s

