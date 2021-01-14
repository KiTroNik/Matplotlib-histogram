from matplotlib import pyplot as plt
import numpy as np


f = open('Dane', 'r')
data = []
for line in f.readlines():
    data.append(float(line.replace(',', '.', 1).rstrip()))
f.close()

fig,ax = plt.subplots(1,1)
a = np.array(data)

ax.hist(a, bins = [5000, 6400, 7800,9200,10600,12000,13400,14800,16200])
ax.set_title("Histogram 5 klas")
ax.set_xticks([5000, 6400, 7800,9200,10600,12000,13400,14800,16200])
plt.savefig("5_klas.png")

fig,ax = plt.subplots(1,1)
ax.hist(a, bins = [5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
ax.set_title("Histogram 10 klas")
ax.set_xticks([5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
plt.savefig("10_klas.png")

fig,ax = plt.subplots(1,1)
ax.hist(a, bins = [5000,5747,6494,7241,7988,8735,9482,10229,10976,11723,12470,13217,13964,14711,15458,16205])
ax.set_title("Histogram 15 klas")
ax.set_xticks([5000,5747,6494,7241,7988,8735,9482,10229,10976,11723,12470,13217,13964,14711,15458,16205])
plt.savefig("15_klas.png")