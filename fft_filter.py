import scipy.fftpack as ft
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
