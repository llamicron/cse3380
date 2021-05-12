import numpy as np
import matplotlib.pyplot as plt

# Load the data
data = np.loadtxt("dataset2.txt")
# All the x values
a = data[:,0]
# Filled in with ones because that's how least-squares works
filled_a = np.vstack([a, np.ones(len(a))]).T
# all the y values
b = data[:,1]
# Compute least-squares
lsq = np.linalg.lstsq(filled_a, b, rcond=None)[0]
print(lsq)
# Plot all (x,y)
plt.plot(a, b, 'ob')

x = np.linspace(0, 0.9, 1)

o = len(lsq)
y = 0
for i in range(o):
    y += lsq[i]*x**i

plt.plot(x, )



# plot the line
# plt.plot(linex, liney, 'ro-', linewidth=2)

plt.show()
