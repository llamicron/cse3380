import numpy as np
import scipy.linalg as linalg

# Create a random 4x4 matrix
A = np.random.randint(-9, 9, (4, 4))
print('Matrix A\n', A)

# Compute the determinant of A
detA = linalg.det(A)
print(f'determinant of A\n', detA)

# Inverse of A
invA = linalg.inv(A)
print('inverse of A\n', invA)

# Rank of A
rankA = np.linalg.matrix_rank(A)
print('rank of A\n', rankA)

# Null space of A
nullA = linalg.null_space(A)
print('Null space\n', nullA)

# solve the matrix equation Ax=b
b = np.random.randint(-9, 9, (4,1))
print('b vector\n', b)

x = linalg.solve(A, b)
print('solved x vector\n', x)

print('A @ x =\n', A @ x)
