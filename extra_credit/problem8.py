import numpy as np
import matplotlib
import matplotlib.pyplot as plt


A = np.array([
    [1, -2],
    [-4, 1]
])
AT = np.transpose(A)

(evalues, evectors) = np.linalg.eig(A)


plt.xlim([-10,10])
plt.ylim([-10,10])

plt.title("Eigenvectors and Eigenvalues")

ax = plt.axes()


plt.show()



