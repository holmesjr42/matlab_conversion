import h5py
import numpy as np
import glob
import os.path as opath
import scipy.io as spio
import csv
import itertools

'''This is not actual conversion for hdf5. This is for the test of the 
conversion with simple examples'''
# fpath = '/home/bhc/codes/matlab_conversion/zt_3_0'
#
# strf_m = glob.glob(opath.join(fpath, '*.mat'))
dataa = []
strf = []

# for i in range(len(strf_m)):
#     # glob treats a path name as a list. use [0] to only load file path
#     dataa = np.ndarray.tolist(spio.loadmat(strf_m[i])['spacepants'][0])
#     strf.append(dataa)
#
# print(strf[1])
# wow = np.array(strf)
# print(wow.shape)
# # 'w' for write, 'a' for preserve and write
#
# with h5py.File('/home/bhc/codes/matlab_conversion/random.hdf5', 'w') as f:
#     f.create_dataset('default', data=wow, dtype='float32')
#
# with h5py.File('/home/bhc/codes/matlab_conversion/random.hdf5', 'r') as f:
#     dato = f['default'][:] #if you add [;], it will assign the database part after you f.close() the hdf5 file
#
#     for key in f.keys(): #retrieving keys
#         koy = []
#         koy.append(key)
#         print(koy)
#
a = [[2, 3], [4, 5]]
b = [[7, 8], [9, 10]]
c = [[11, 12], [13, 14]]
f = [[[2, 3], [4, 5]], [[7, 8], [9, 10]]]
e = [a, b, c]
# e = list(itertools.chain(*e))
d = ['one', 'two', 'three']
print(len(e))


#
hdf5_file = h5py.File('/home/bhc/codes/matlab_conversion/random.hdf5', mode='w')
dt = h5py.special_dtype(vlen=np.dtype('float64'))

for i in d:
    hdf5_file.create_dataset(i, (2, 2), dtype=dt)

# hdf5_file.create_dataset(d[1], (len(e),), dtype=dt)
# hdf5_file.create_dataset(d[2], (len(e),), dtype=dt)

for i in range(3):
    for j in range(2):
         hdf5_file[d[i]][j] = f[1]
         # print(f[1][1])
         print(hdf5_file[d[i]][j])


print(hdf5_file['one'][0])


'''
this is for finding corresponding order array elements to the other array with a certain boolean condition
a = np.arange(10)
b = np.arange(11, 21)
data = a[b > 15] # or a[b[:]>15]
print(data,a ,b)

Another example with a huge dataset

with h5py.File('complex_read.hdf5', 'r') as f:
    d1 = f['array_1']
    d2 = f['array_2']

    data = []

    for i in range(len(d1)):
        if d1[i] > 0:
            data.append(d2[i])

print('The length of data with a for loop: {}'.format(len(data)))

'''