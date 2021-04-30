"""
Luke Sweeney
1001764631
April 30, 2021
CSE 3380
"""

import numpy
import matplotlib
import matplotlib.pyplot as plt


# Part A
# Not sure at all if i did this right :(
def loss_plot():
    u = [numpy.random.randint(-50, 50, (1,1)) for _ in range(100)]
    v = [numpy.random.randint(-50, 50, (1,1)) for _ in range(100)]
    x = []
    l1 = []
    l2 = []
    for i in range(100):
        x.append(u[i][0][0] - v[i][0][0])
        l = loss(u[i], v[i])
        l1.append(l[0])
        l2.append(l[1])
    plt.title("u-v vs. L1 and L2 loss")
    plt.xlabel("u-v")
    plt.ylabel("L1 and L2 loss")
    plt.plot(x, l1)
    plt.plot(x, l2)
    plt.show()

# Part B
def loss(u, v):
    """
    Returns the L1 and L2 loss as a tuple
    """
    l1 = 0
    l2 = 0

    for i in range(len(u)):
        l1 += abs(u[i] - v[i])
        l2 += (u[i] - v[i]) ** 2
    
    print(f'L1 loss = {l1}, L2 loss = {l2}')
    
    return (l1, l2)

# Part C
def loss_test():
    print("Testing with random 4x1 matrices")
    u = numpy.random.randint(-9, 9, (4,1))
    v = numpy.random.randint(-9, 9, (4,1))
    print(u)
    print(v)
    loss(u, v)


if __name__ == '__main__':
    loss_plot()
    loss_test()
