"""
Luke Sweeney
1001764631
CSE 3380
Extra Credit
"""
import numpy as np
import matplotlib.pyplot as plt

# Load the data
data = np.loadtxt("dataset1.txt")
# All the x values
a = data[:,0]
# Filled in with ones because that's how least-squares works
filled_a = np.vstack([a, np.ones(len(a))]).T
# all the y values
b = data[:,1]
# Compute least-squares
lsq = np.linalg.lstsq(filled_a, b, rcond=None)[0]
# Plot all (x,y)
plt.plot(a, b, 'ob')

# Get the line start and end x values
linex = [0, a[-1]]
# Get the line start and end y values (b, mx + b)
liney = [lsq[1], lsq[0] * a[-1] + lsq[1]]

# plot the line
plt.plot(linex, liney, 'ro-', linewidth=2)

plt.show()
