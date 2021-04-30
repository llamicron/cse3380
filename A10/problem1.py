"""
Luke Sweeney
1001764631
April 30, 2021
CSE 3380
"""
from numpy import dot
from numpy.linalg import norm

# Part A
def cosine_sim(u, v):
    """
    Find the cosine similarity between two vectors u and v

    Example:
        assert cosine_sim(
            [1, 1], 
            [-1, -1]
        ) == -1
    """
    return dot(u, v) / (norm(u) * norm(v))
    

# Testing Part A
def test_cosine_sim():
    # Opposite
    set1 = ( [1, 1], [-1, -1] )
    # Same
    set2 = ( [1, 1], [1, 1] )
    # Orthogonal
    set3 = ( [-1, 1], [1, 1] )
    
    assert round(cosine_sim(*set1)) == -1
    assert round(cosine_sim(*set2)) == 1
    assert round(cosine_sim(*set3)) == 0

# Part B
def part_b():
    set1 = ( [3, -1, 4], [-2, 3, 1] )
    set2 = ( [5, 6, -5], [6, 2, -5] )
    set3 = ( [-3, 1, 7], [7, -4, 7] )

    print(f"Set 1 = {cosine_sim(*set1)}")
    print(f"Set 2 = {cosine_sim(*set2)}")
    print(f"Set 3 = {cosine_sim(*set3)}")


# Run the tests and part B
if __name__ == '__main__':
    print("Testing...", end='');
    test_cosine_sim()
    print('passed.')
    part_b()
