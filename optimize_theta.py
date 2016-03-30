#!/usr/bin/env python

import subprocess
import sys
import time
import pandas as pd
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

for i in range(0, 1000, 10):
    for j in range(0, 1000, 10):
        io = i/1000.
        jo = j/1000.
    results.append(run_with_theta(io, jo))
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
ax = fig.add_subplot(111, projection='3d')

ax.scatter(xs, ys, zs)

plt.show()
