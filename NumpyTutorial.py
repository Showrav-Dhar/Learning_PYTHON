import numpy as np
import time
import sys

if __name__ == '__main__':
    # l = range(1000)  # making a list which size is 1000
    # print(sys.getsizeof(1) * len(l))
    #
    # ara = np.arange(1000)  # making a array of 1000 length,arange = range for list
    # print(ara.size * ara.itemsize)
    # ara.size = total length of array
    # ara.itemize = size of one item
    # numpy array will be lower in size than traditional python array

    # proving why numpy array are faster than python list
    sz = 100000

    l1 = range(sz)
    l2 = range(sz)

    a1 = np.arange(sz)
    a2 = np.arange(sz)

    # checking time for computing python list
    start = time.time()
    res = [(x + y) for x, y in zip(l1, l2)]
    # takes one item from l1 and one item from l2 and adds them and stores them in res list
    print("Python list took = ", (time.time() - start) * 1000)

    # checking time for computing numpy array
    start = time.time()
    res = a1 + a2  # does same as above list comprehension
    print("numpy array took = ", (time.time() - start) * 1000)

    # after executing the program -
    # Python list took = 15.7470703125
    # numpy array took = 4.986047744750977
