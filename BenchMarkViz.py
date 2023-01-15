import matplotlib.pyplot as plt

# note that the data is from BenchMark.py

# insert benchmark
x = [500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
k1 = [0.03, 0.18, 0.78, 1.63, 3.17, 4.71, 6.8, 9.6, 12.45, 15.71, 16.47]
k2 = [0.12, 0.53, 2.03, 4.24, 7.45, 10.94, 18.1, 23.84, 36.06, 46.61, 56.87]
plt.plot(x,k1,'s-',color = 'r',label="insert from min to max")
plt.plot(x,k2,'o-',color = 'g',label="insert from max to min")
plt.xlabel("insert count")
plt.ylabel("time(s)")
plt.legend(loc = "best")
plt.show()

# delMin benchmark
x = [500, 1000, 2000, 3000, 4000, 5000, 6000, 7000]
k1 = [0.15, 0.65, 2.52, 4.93, 11.9, 19.12, 24.29, 30.66]
k2 = [0.18, 0.56, 2.26, 4.34, 10.02, 15.96, 18.69, 27.0]
plt.plot(x,k1,'s-',color = 'r',label="delMin from min to max")
plt.plot(x,k2,'o-',color = 'g',label="delMin from max to min")
plt.xlabel("node count")
plt.ylabel("time(s)")
plt.legend(loc = "best")
plt.show()

