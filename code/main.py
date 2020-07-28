import numpy as np
import pandas as pd

data = pd.read_csv("blocks51.txt", header=None)

aa = []
k = 0
l = 0
for i, j in data.iterrows():
    if k == 0:
        block = j
    if k != 0:
        block = np.vstack((block, j))
    k += 1

    if k == 3:
        aa.append(block)

        k = 0
        if l == 0:
            bb = block
        else:
            bb = np.hstack((bb, block))
        l += 1
        block = []
ll = []
for i in bb.T:
    ll.append(tuple(i))

my_set = set()
for l in ll:
    my_set.add(l)
k = 1
for i in my_set:
    print(k, 'Vector', i, 'repeats', ll.count(i), 'times')
    k += 1

pairs = set()
temp = []
for i in aa:
    i = i.T
    for j in range(len(i) - 1):
        t1 = tuple(np.hstack((i[j], i[j + 1])))
        t2 = tuple(np.hstack((i[j + 1], i[j])))
        temp.append(t1)
        temp.append(t2)
        pairs.add(t1)
        pairs.add(t2)
k = 1
for i in pairs:
    print(k, 'Pair', i, 'repeats', temp.count(i), 'times')
    k += 1
