import numpy


"""
Test if two vectors are orthogonal
if u * v = 0, then they're orthogonal (dot product)
"""
# There are orthogonal
u = numpy.array([0, 1])
v = numpy.array([1, 0])
assert numpy.dot(u, v) == 0

# These are not
u = numpy.array([4, 7, 6])
v = numpy.array([2, 3, 6])
assert numpy.dot(u, v) != 0


"""
Normalize a vector
"""
# The vector u
u = numpy.array([4, 7, 6])
# The normalized vector u / ||u||
norm_u = u / numpy.linalg.norm(u)

