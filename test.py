import numpy as np
import pickle
import os
from collections import Counter
import h5py
k = sorted(snakemake.input.lfp)
e = sorted(snakemake.input.tsp)
l = []

for i in range(len(k)):
    print(k[i])
#     p = k[i].split('/')
#     l.append(p[13])
# t = Counter(l)
# tl = list(t.keys())
# print(tl)

# prots = set(prots)
# print(prots)
b = 'hey'
#
with open(snakemake.output[0]) as c:
    c.write(b)

# k = os.listdir("/home/bhc/OneDrive/Work/PhD/projects/zwicker_tone_2018_2021/data/dataset/raw/cr100_990909/tsp/")
#
# print(k)
