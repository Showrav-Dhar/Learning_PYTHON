import numpy as np
import time
import sys

if __name__ == '__main__':

    sz = 10000

    test_list = range(sz)
    print(sys.getsizeof(1)*len(test_list))

    test_arra = np.arange(sz)
    print(test_arra.size*test_arra.itemsize)



    l1 = range(sz)
    l2 = range(sz)

    start = time.time()
    res = [(x+y) for x,y in zip(l1,l2)]
    print("list took time - (in Ms)",(time.time()-start)*1000)

    a1 = np.arange(sz)
    a2 = np.arange(sz)

    start = time.time()
    res = a1+a2
    print("numpy array took time - (in Ms)", (time.time() - start) * 1000)


