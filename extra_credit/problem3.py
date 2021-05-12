"""
Luke Sweeney
1001764631
CSE 3380
Extra Credit
"""
from scipy import linalg
import numpy


A = numpy.array([
    [1, 0, 4],
    [-2, 3, -2],
    [-2, 0, 6]
])

(Q, R) = linalg.qr(A)

# According to the formula, we should take Q @ R and get A
# I can't (easily) directly compare them here 
# because there are small floating point errors
print('A =\n', A)
print('Q * R =\n', Q @ R)

# This checks out on paper too. I tried to calculate Q by hand but kept getting
# and incorrect answer and the final is in a few hours so I'm gonna stop here lmao.

