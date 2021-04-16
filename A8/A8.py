# Luke Sweeney
# 1001764631
# CSE 3380 - Linear Algebra
# Professor Dillhoff
# A8 - April 9, 2021
import numpy as np
import scipy.linalg as linalg
import sympy

A = np.array([
    [-7, 0, -3],
    [7, -1, 0],
    [5, -1, 0]
])
b = np.array([-10, 5, 3])



def partA():
    """
    Part A

    Compute the reduced echelon form of A and convert the result back to a numpy array.
    """
    print('Part A')
    # Concert from numpy to sympy
    A_sympy = sympy.Matrix(A)
    # Grab the rref and pivots
    (A_rref, _) = A_sympy.rref()
    # Convert back to numpy
    A_rref = np.array(A_rref)
    # Print the rref
    print(f'RREF(A) =\n{A_rref}\n\n')



def partB():
    """
    Part B

    Find the column space of A
    """
    # Sympy has a columnspace() method
    print('Part B')
    # Convert to sympy, get the column space, and print each one
    # yay list comprehension
    [print(vec) for vec in sympy.Matrix(A).columnspace()]
    print('\n\n')

def partC():
    """
    Part C

    Solve the matrix equation Ax = b
    """
    print('Part C')
    # Use linalg to solve the matrix equation
    x = linalg.solve(A, b)
    # print x
    print(f'x = {x}\n\n')



def partD():
    """
    Part D

    Compute Nul A
    """
    # Sympy has a nullspace() method just like in part B
    print('Part D')
    # Convert to sympy, get the null space, and print each one
    # yay list comprehension
    [print(vec) for vec in sympy.Matrix(A).nullspace()]
    print("There are no vectors in Nul A")
    print('\n\n')



if __name__ == '__main__':
    partA()
    partB()
    partC()
    partD()
