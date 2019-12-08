# Name : FNU Rahasya Chandan
# UTA Id: 1000954962
#: Notch Filter

import numpy as np 
import matplotlib.pyplot as plt # matlab plotting in python

#Load data from a file, with missing values handled using delimeter
data = np.genfromtxt('notchData.csv', delimiter=',')
x = np.append(data, np.zeros(100))   # new array with a copy

f = 17  # normalized radian frequency
fs = 500    # samping frequency
w = (2*np.pi*f)/fs

#y[n] = 0 when n < 0
#x[n] = 0 when n < 0 or N − 1 < n
y = np.zeros(len(x))
y[0] = x[0]
y[1] = x[1]

n = 2

for n in range(len(y)):
	y[n] = 1.8744*np.cos(w)*y[n-1]-0.8783*y[n-2] + x[n] - 2*np.cos(w)*x[n-1] + x[n-2]

# plot the original signal
plt.figure()
plt.title("Original Signal x")
plt.plot(data)
# x-axis limited to [-25, 625]
plt.xlim(-25, 625)

# plot the filtered signal
plt.figure()
plt.title("Filtered Signal y")
plt.plot(y)
# y-axis limited to [-2.25, 2.25]
plt.ylim(-2.25, 2.25)

# plot the combined signal
plt.figure()
plt.title("Combined Signal = 10 Hz + 33 Hz")
a = np.arange(0,len(y),1)
s1 = np.cos(2*np.pi*10*(a/fs)) # signal 1 = 10
s2 = np.cos(2*np.pi*33*(a/fs)) # signal 2 = 33
plt.plot(a, s1+s2)
# x-axis limited to [-25, 625]
plt.xlim(-25, 625)

plt.show()