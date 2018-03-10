#-

import matplotlib as mpl
import matplotlib.pyplot as plt
import os

f1_data1 = {}
f1_data2 = {}
with open("C:\\Users\\재원\\Desktop\\sample.txt", "r") as f1:
    str = f1.read().split("\n")

    for line in str:
        items = line.split("\t")
        print (items)
        data = [items[1], items[2]]

        if not (data[0] in f1_data1):
            f1_data1[data[0]] = []

        if not (data[1] in f1_data2):
            f1_data2[data[1]] = []

        f1_data1[data[0]].append(float(items[1]))
        f1_data2[data[1]].append(float(items[2]))

mpl.use('Agg')

plt.plot(f1_data1)
plt.savefig("./result.png")
plt.close()