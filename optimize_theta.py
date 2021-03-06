#!/usr/bin/env python

import subprocess
import sys
import time
import pandas as pd
import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

def run_with_theta(t, s):
    ts, ss = str(t), str(s)
    run_process = subprocess.Popen(
        ['./rerank-baseline', '-t', ts, '-s', ss],
        stdout=subprocess.PIPE)

    output = subprocess.check_output(['./compute-bleu'], stdin=run_process.stdout)
    val = float(output)

    return [t, s, val]

results = []

for i in numpy.random.randn(5)/2. - 0.5:
    for j in numpy.random.randn(5)/2. - 0.5:
        results.append(run_with_theta(i, j))
# for i in range(0, 1000, 100):
#     for j in range(0, 1000, 100):
#         io = i/1000.
#         jo = j/1000.
#         results.append(run_with_theta(io, jo))
#
# rpd = pd.DataFrame()
# rpd.append([{
#     'x': r[0],
#     'y': r[1],
#     'z': r[2]
# } for r in results])
#
# sns.heatmap(rpd)
# plt.show()

xs = [r[0] for r in results]
ys = [r[1] for r in results]
zs = [r[2] for r in results]

fig = plt.figure()
ax = fig.add_subplot(111)
#
# ax.scatter(xs, ys, c=zs)

rpd = pd.DataFrame.from_items([('x', xs), ('y', xs), ('z', xs)])
sns.heatmap(rpd)
plt.show()
