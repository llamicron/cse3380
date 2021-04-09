import numpy as np


# Create two 3x3 matrices of random integers in range [-9,9]
A = np.random.randint(-9, 9, (3,3))
B = np.random.randint(-9, 9, (3,3))

# Element wise multiplication
C = A * B
# Matrix multiplication
C = A @ B

# Create a 3x3 matrix
inline = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# A few other useful things
# Array of ones
# np.ones()
# Array of zeroes
# np.zeros()
