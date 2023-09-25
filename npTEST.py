import numpy as np
import time
import sys

if __name__ == '__main__':

    sz = 1000000

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


