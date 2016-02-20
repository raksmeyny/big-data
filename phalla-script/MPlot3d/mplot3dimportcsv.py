from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
import csv

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

my_data = genfromtxt('time_post.csv', delimiter=',')

# x = my_data[:,1]
# y = my_data[:,2]
# z = my_data[:,3]


# xpos = x.flatten()
# ypos = y.flatten()
# zpos = z.flatten()
# dx = y
# dy = dx.copy()
# dz = x.flatten()

# ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')

points1X = my_data[:,1]
points1Y = my_data[:,2]
points1Z = my_data[:,3]

## I remove the header of the CSV File.
points1X = np.delete(points1X, 0)
points1Y = np.delete(points1Y, 0)
points1Z = np.delete(points1Z, 0)

# Convert the array to 1D array
points1X = np.reshape(points1X,points1X.size)
points1Y = np.reshape(points1Y,points1Y.size)
points1Z = np.reshape(points1Z,points1Z.size)

ax.plot(points1X, points1Y, points1Z, 'd', markersize=8, markerfacecolor='red', label='points1')

plt.show()