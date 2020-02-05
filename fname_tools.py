import glob
import os.path as opath
import numpy as np
import os

'''
Tools to order the file names

prot: list of protocols aka folder names in one animal
path_1: f_path, or the main path to the file/folder location
animal: the name of data folder which follows animal number/date
path_2: the path list which contains tsp and lfp

'''

'''
nnm
'''


def nnm_o(prot, path_1, animal, path_2):

    for i_file in prot:
        files_nnm_l = []
        files_nnm_t = []
        d_path_l = glob.glob(opath.join(path_1 + animal + path_2[0] + i_file))
        files_nnm_l = np.append(files_nnm_l, d_path_l)
        d_path_t = glob.glob(opath.join(path_1 + animal + path_2[1] + i_file))
        files_nnm_t = np.append(files_nnm_t, d_path_t)


# p_n = file_name

# lfp

        for i in range(len(files_nnm_l)):
            for p_n in os.listdir(files_nnm_l[i]):
                if p_n.endswith('.mat'):
                    if p_n[0:2] != 'LF':
                        print("It's already done")
                        break
                    elif p_n[-6:-4] == '70':
                        os.rename(opath.join(files_nnm_l[i] + '/' + p_n),
                                  opath.join(files_nnm_l[i] + '/'
                                             + p_n.replace('LFP', '01_lfp')))
                    elif p_n[-6:-4] == '60':
                        os.rename(opath.join(files_nnm_l[i] + '/' + p_n),
                                  opath.join(files_nnm_l[i] + '/'
                                             + p_n.replace('LFP', '02_lfp')))
                    elif p_n[-6:-4] == '50':
                        os.rename(opath.join(files_nnm_l[i] + '/' + p_n),
                                  opath.join(files_nnm_l[i] + '/'
                                             + p_n.replace('LFP', '03_lfp')))
                    elif p_n[-6:-4] == '40':
                        os.rename(opath.join(files_nnm_l[i] + '/' + p_n),
                                  opath.join(files_nnm_l[i] + '/'
                                             + p_n.replace('LFP', '04_lfp')))
                    elif p_n[-6:-4] == '30':
                        os.rename(opath.join(files_nnm_l[i] + '/' + p_n),
                                  opath.join(files_nnm_l[i] + '/'
                                             + p_n.replace('LFP', '05_lfp')))
                    else:
                        print(p_n, ' has nothing to change')

# tsp
        for i in range(len(files_nnm_t)):
            for p_n in os.listdir(files_nnm_t[i]):
                if p_n[0:2] != 'Ts':
                    print("It's already done")
                    break
                elif p_n[-6:-4] == '70':
                    os.rename(opath.join(files_nnm_t[i] + '/' + p_n),
                              opath.join(files_nnm_t[i] + '/'
                                         + p_n.replace('Tsp', '01_tsp')))
                elif p_n[-6:-4] == '60':
                    os.rename(opath.join(files_nnm_t[i] + '/' + p_n),
                              opath.join(files_nnm_t[i] + '/'
                                         + p_n.replace('Tsp', '02_tsp')))
                elif p_n[-6:-4] == '50':
                    os.rename(opath.join(files_nnm_t[i] + '/' + p_n),
                              opath.join(files_nnm_t[i] + '/'
                                         + p_n.replace('Tsp', '03_tsp')))
                elif p_n[-6:-4] == '40':
                    os.rename(opath.join(files_nnm_t[i] + '/' + p_n),
                              opath.join(files_nnm_t[i] + '/'
                                         + p_n.replace('Tsp', '04_tsp')))
                elif p_n[-6:-4] == '30':
                    os.rename(opath.join(files_nnm_t[i] + '/' + p_n),
                              opath.join(files_nnm_t[i] + '/'
                                         + p_n.replace('Tsp', '05_tsp')))
                else:
                    print(p_n, ' has nothing to change')


'''
nn
'''


def nn_o(prot, path_1, animal, path_2):

    for i_file in prot:
        files_nn_l = []
        files_nn_t = []
        d_path_l = glob.glob(opath.join(path_1 + animal + path_2[0] + i_file))
        files_nn_l = np.append(files_nn_l, d_path_l)
        d_path_t = glob.glob(opath.join(path_1 + animal + path_2[1] + i_file))
        files_nn_t = np.append(files_nn_t, d_path_t)

# p_n = file_name

# lfp

        for i in range(len(files_nn_l)):
            for p_n in os.listdir(files_nn_l[i]):
                if p_n.endswith('.mat'):
                    if p_n[0:2] != 'LF':
                        print("It's already done")
                        break
                    elif p_n[-17:-15] == '70':
                        os.rename(opath.join(files_nn_l[i] + '/' + p_n),
                                  opath.join(files_nn_l[i] + '/'
                                             + p_n.replace('LFP', '01_lfp')))
                    elif p_n[-17:-15] == '60':
                        os.rename(opath.join(files_nn_l[i] + '/' + p_n),
                                  opath.join(files_nn_l[i] + '/'
                                             + p_n.replace('LFP', '02_lfp')))
                    else:
                        print(p_n, ' has nothing to change')

# tsp
        for i in range(len(files_nn_t)):
            for p_n in os.listdir(files_nn_t[i]):
                if p_n.endswith('.mat'):
                    if p_n[0:2] != 'Ts':
                        print("It's already done")
                        break
                    elif p_n[-17:-15] == '70':
                        os.rename(opath.join(files_nn_t[i] + '/' + p_n),
                                  opath.join(files_nn_t[i] + '/'
                                             + p_n.replace('Tsp', '01_tsp')))
                    elif p_n[-17:-15] == '60':
                        os.rename(opath.join(files_nn_t[i] + '/' + p_n),
                                  opath.join(files_nn_t[i] + '/'
                                             + p_n.replace('Tsp', '02_tsp')))
                    else:
                        print(p_n, ' has nothing to change')


'''
strf
'''


def strf_o(prot, path_1, animal, path_2):

    for i_file in prot:
        files_strf_l = []
        files_strf_t = []
        d_path_l = glob.glob(opath.join(path_1 + animal + path_2[0] + i_file))
        files_strf_l = np.append(files_strf_l, d_path_l)
        d_path_t = glob.glob(opath.join(path_1 + animal + path_2[1] + i_file))
        files_strf_t = np.append(files_strf_t, d_path_t)

# p_n = file_name

# lfp

        for i in range(len(files_strf_l)):
            for p_n in os.listdir(files_strf_l[i]):
                if p_n.endswith('.mat'):
                    if p_n[0:2] != 'LF':
                        print("It's already done")
                        break
                    elif p_n[-18:-16] == '70':
                        os.rename(opath.join(files_strf_l[i] + '/' + p_n),
                                  opath.join(files_strf_l[i] + '/'
                                             + p_n.replace('LFP', '01_lfp')))
                    elif p_n[-18:-16] == '60':
                        os.rename(opath.join(files_strf_l[i] + '/' + p_n),
                                  opath.join(files_strf_l[i] + '/'
                                             + p_n.replace('LFP', '02_lfp')))
                    elif p_n[-18:-16] == '50':
                        os.rename(opath.join(files_strf_l[i] + '/' + p_n),
                                  opath.join(files_strf_l[i] + '/'
                                             + p_n.replace('LFP', '03_lfp')))
                    elif p_n[-18:-16] == '40':
                        os.rename(opath.join(files_strf_l[i] + '/' + p_n),
                                  opath.join(files_strf_l[i] + '/'
                                             + p_n.replace('LFP', '04_lfp')))
                    elif p_n[-18:-16] == '30':
                        os.rename(opath.join(files_strf_l[i] + '/' + p_n),
                                  opath.join(files_strf_l[i] + '/'
                                             + p_n.replace('LFP', '05_lfp')))
                    else:
                        print(p_n, ' has nothing to change')

# tsp
        for i in range(len(files_strf_t)):
            for p_n in os.listdir(files_strf_t[i]):
                if p_n.endswith('.mat'):
                    if p_n[0:2] != 'Ts':
                        print("It's already done")
                        break
                    elif p_n[-18:-16] == '70':
                        os.rename(opath.join(files_strf_t[i] + '/' + p_n),
                                  opath.join(files_strf_t[i] + '/'
                                             + p_n.replace('Tsp', '01_tsp')))
                    elif p_n[-18:-16] == '60':
                        os.rename(opath.join(files_strf_t[i] + '/' + p_n),
                                  opath.join(files_strf_t[i] + '/'
                                             + p_n.replace('Tsp', '02_tsp')))
                    elif p_n[-18:-16] == '50':
                        os.rename(opath.join(files_strf_t[i] + '/' + p_n),
                                  opath.join(files_strf_t[i] + '/'
                                             + p_n.replace('Tsp', '03_tsp')))
                    elif p_n[-18:-16] == '40':
                        os.rename(opath.join(files_strf_t[i] + '/' + p_n),
                                  opath.join(files_strf_t[i] + '/'
                                             + p_n.replace('Tsp', '04_tsp')))
                    elif p_n[-18:-16] == '30':
                        os.rename(opath.join(files_strf_t[i] + '/' + p_n),
                                  opath.join(files_strf_t[i] + '/'
                                             + p_n.replace('Tsp', '05_tsp')))
                    else:
                        print(p_n, ' has nothing to change')


'''
tc
'''
# funciton for zwicker tone

def tc_o(prot, path_1, animal, path_2):

    for i_file in prot:
        files_tc_l = []
        files_tc_t = []
        d_path_l = glob.glob(opath.join(path_1 + animal + path_2[0] + i_file))
        files_tc_l = np.append(files_tc_l, d_path_l)
        d_path_t = glob.glob(opath.join(path_1 + animal + path_2[1] + i_file))
        files_tc_t = np.append(files_tc_t, d_path_t)

# p_n = file_name

# lfp

        for i in range(len(files_tc_l)):
            for p_n in os.listdir(files_tc_l[i]):
                if p_n.endswith('.mat'):
                    tcs = p_n.split('-')
                    numb_1 = str(tcs[3])
                    numb_2 = numb_1.zfill(3)
                    os.rename(opath.join(
                                         files_tc_l[i] + '/' + tcs[0] + '-'
                                         + tcs[1] + '-' + tcs[2] + '-'
                                         + tcs[3] + '-' + tcs[4]
                                        ),
                              opath.join(
                                         files_tc_l[i] + '/' + tcs[0] + '-'
                                         + tcs[1] + '-' + tcs[2] + '-'
                                         + tcs[3].replace(str(numb_1)
                                                          , str(numb_2))
                                         + '-' + tcs[4]
                                        )
                              )
# tsp

            for p_n in os.listdir(files_tc_t[i]):
                if p_n.endswith('.mat'):
                    tcs = p_n.split('-')
                    numb_1 = str(tcs[3])
                    numb_2 = numb_1.zfill(3)
                    os.rename(opath.join(
                                         files_tc_t[i] + '/' + tcs[0] + '-'
                                         + tcs[1] + '-' + tcs[2] + '-'
                                         + tcs[3] + '-' + tcs[4]
                                        ),
                              opath.join(
                                       files_tc_t[i] + '/' + tcs[0] + '-'
                                       + tcs[1] + '-' + tcs[2] + '-'
                                       + tcs[3].replace(str(numb_1)
                                                        , str(numb_2))
                                       + '-' + tcs[4]
                                      )
                              )


# function for gabazine

def tcg_o(prot, path_1, animal, path_2):

    for i_file in prot:
        files_tc_l = []
        files_tc_t = []
        d_path_l = glob.glob(opath.join(path_1 + animal + path_2[0] + i_file))
        files_tc_l = np.append(files_tc_l, d_path_l)
        d_path_t = glob.glob(opath.join(path_1 + animal + path_2[1] + i_file))
        files_tc_t = np.append(files_tc_t, d_path_t)

# p_n = file_name

# lfp

        for i in range(len(files_tc_l)):
            for p_n in os.listdir(files_tc_l[i]):
                if p_n.endswith('.mat'):
                    if p_n[0:2] != 'LF':
                        print("It's already done")
                        break
                    elif p_n[-9:-7] == '70':
                        os.rename(opath.join(files_tc_l[i] + '/' + p_n),
                                  opath.join(files_tc_l[i] + '/'
                                             + p_n.replace('LFP', '01_lfp')))
                    elif p_n[-9:-7] == '60':
                        os.rename(opath.join(files_tc_l[i] + '/' + p_n),
                                  opath.join(files_tc_l[i] + '/'
                                             + p_n.replace('LFP', '02_lfp')))
                    elif p_n[-9:-7] == '50':
                        os.rename(opath.join(files_tc_l[i] + '/' + p_n),
                                    opath.join(files_tc_l[i] + '/'
                                               + p_n.replace('LFP', '03_lfp')))
                    elif p_n[-9:-7] == '40':
                        os.rename(opath.join(files_tc_l[i] + '/' + p_n),
                                  opath.join(files_tc_l[i] + '/'
                                             + p_n.replace('LFP', '04_lfp')))
                    elif p_n[-9:-7] == '30':
                        os.rename(opath.join(files_tc_l[i] + '/' + p_n),
                                  opath.join(files_tc_l[i] + '/'
                                             + p_n.replace('LFP', '05_lfp')))
                    else:
                        print(p_n, ' has nothing to change')


# tsp

        for i in range(len(files_tc_t)):
            for p_n in os.listdir(files_tc_t[i]):
                if p_n.endswith('.mat'):
                    if p_n[0:2] != 'Ts':
                        print("It's already done")
                        break
                    elif p_n[-9:-7] == '70':
                        os.rename(opath.join(files_tc_t[i] + '/' + p_n),
                                  opath.join(files_tc_t[i] + '/'
                                             + p_n.replace('Tsp', '01_tsp')))
                    elif p_n[-9:-7] == '60':
                        os.rename(opath.join(files_tc_t[i] + '/' + p_n),
                                  opath.join(files_tc_t[i] + '/'
                                             + p_n.replace('Tsp', '02_tsp')))
                    elif p_n[-9:-7] == '50':
                        os.rename(opath.join(files_tc_t[i] + '/' + p_n),
                                  opath.join(files_tc_t[i] + '/'
                                             + p_n.replace('Tsp', '03_tsp')))
                    elif p_n[-9:-7] == '40':
                         os.rename(opath.join(files_tc_t[i] + '/' + p_n),
                                   opath.join(files_tc_t[i] + '/'
                                              + p_n.replace('Tsp', '04_tsp')))
                    elif p_n[-9:-7] == '30':
                        os.rename(opath.join(files_tc_t[i] + '/' + p_n),
                                  opath.join(files_tc_t[i] + '/'
                                             + p_n.replace('Tsp', '05_tsp')))
                    else:
                        print(p_n, ' has nothing to change')


'''
sil
'''


def sil_o(prot, path_1, animal, path_2):



    for i_file in prot:
        files_sil_l = []
        files_sil_t = []
        d_path_l = glob.glob(opath.join(path_1 + animal + path_2[0] + i_file))
        files_sil_l = np.append(files_sil_l, d_path_l)
        d_path_t = glob.glob(opath.join(path_1 + animal + path_2[1] + i_file))
        files_sil_t = np.append(files_sil_t, d_path_t)


# # p_n = file_name

# lfp

        for i in range(len(files_sil_l)):
            for p_n in os.listdir(files_sil_l[i]):
                if p_n.endswith('.mat'):
                    tcs = p_n.split('-')
                    numb_1 = str(tcs[3])
                    numb_2 = numb_1.zfill(3)
                    os.rename(opath.join(
                                         files_sil_l[i] + '/' + tcs[0] + '-'
                                         + tcs[1] + '-' + tcs[2] + '-'
                                         + tcs[3] + '-' + tcs[4]
                                        ),
                              opath.join(
                                         files_sil_l[i] + '/' + tcs[0] + '-' +
                                         tcs[1] + '-' + tcs[2] + '-'
                                         + tcs[3].replace(str(numb_1),
                                                          str(numb_2))
                                         + '-' + tcs[4]
                                        )
                              )

# tsp
        for i in range(len(files_sil_t)):
            for p_n in os.listdir(files_sil_t[i]):
                if p_n.endswith('.mat'):
                    tcs = p_n.split('-')
                    numb_1 = str(tcs[3])
                    numb_2 = numb_1.zfill(3)
                    os.rename(opath.join(
                                         files_sil_t[i] + '/' + tcs[0] + '-'
                                         + tcs[1] + '-' + tcs[2] + '-'
                                         + tcs[3] + '-' + tcs[4]
                                        ),
                              opath.join(
                                         files_sil_t[i] + '/' + tcs[0] + '-'
                                         + tcs[1] + '-' + tcs[2] + '-'
                                         + tcs[3].replace(str(numb_1),
                                                          str(numb_2))
                                         + '-' + tcs[4]
                                        )
                              )
