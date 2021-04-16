# Luke Sweeney
# CSE 3380 - Professor Dillhoff
# A9 - April 16, 2021
# ID: 1001764631
import sympy
import itertools

def main():
    """
    Checks the hand calculated expected values against the
    calculated values. Throws an AssertionError if they're not the same.
    """

    # B matrix, given in problem 2
    B = sympy.Matrix([
        [-3, 1, 5],
        [6, 8, 5],
        [2, -4, -2],
    ])
    # C matrix, given in problem 2
    C = sympy.Matrix([
        [1, 1, -7],
        [-8, 5, 1],
        [-8, 8, -1],
    ])

    # P (C <- B) expected value, calculated by hand
    B_to_C_expected = sympy.Matrix([
        [-219/139, -597/139, -412/139],
        [-184/139, -692/139, -475/139],
        [2/139, -204/139, -226/139]
    ])
    # P (B <- C) expected value, calculated by hand
    C_to_B_expected = sympy.Matrix([
        [-214/95, 183/95, 11/190],
        [153/95, -181/95, 203/190],
        [-28/19, 33/19, -30/19]
    ])

    # Get sympy to calculate the actual value
    B_to_C = C.inv() @ B
    # And calculate the inverse
    C_to_B = B_to_C.inv()

    # For each entry in the calculated matrix and the expected matrix
    for i, j in itertools.product(range(3), range(3)):
        # make sure the difference is 0
        # We can't compare directly because of tiny inaccuracies
        # Subtracting rounds a bit and it goes to 0
        assert (B_to_C[i, j] - B_to_C_expected[i, j]) == 0
    # Same thing for the C_to_B matrix
    for i, j in itertools.product(range(3), range(3)):
        assert (C_to_B[i, j] - C_to_B_expected[i, j]) == 0
    
    print("All good.")


if __name__ == '__main__':
    main()
    