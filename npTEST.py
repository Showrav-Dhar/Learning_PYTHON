import numpy as np
import sys
import time

if __name__ == '__main__':
    # sz = 10000
    #
    # test_list = range(sz)
    # print(sys.getsizeof(1)*len(test_list))
    #
    # test_arra = np.arange(sz)
    # print(test_arra.size*test_arra.itemsize)
    #
    #
    #
    # l1 = range(sz)
    # l2 = range(sz)
    #
    # start = time.time()
    # res = [(x+y) for x,y in zip(l1,l2)]
    # print("list took time - (in Ms)",(time.time()-start)*1000)
    #
    # a1 = np.arange(sz)
    # a2 = np.arange(sz)
    #
    # start = time.time()
    # res = a1+a2
    # print("numpy array took time - (in Ms)", (time.time() - start) * 1000)

    # video 2 - basic array operations
    #     a = np.array([[1,2],[3,4],[5,6]],dtype=np.float64)
    #     print(a)
    #     print(a.shape)
    #     print(a.dtype)
    #     print(a.itemsize)
    #     print(a.ndim)
    #     print(a.size)
    #     b = np.array([[1, 2], [3, 10], [100, 6]], dtype=complex)
    #     print(b.dtype)

    # print("HELLO")
    # a = np.array([[1,2],[3,4],[4,5]])
    # print("Shape of a = ",a.shape)
    # print(a)
    #
    # b = a.reshape(2,3)
    # print("Changed shape of a = ",b.shape)
    # print(b)

    # a = np.zeros((4,4))
    # print(a)
    a = np.array([[9, 4], [25, 36], [49, 64]])
    print(np.sqrt(a))
    print(np.std(a))
    print(a.sum(axis=0))  # axis = 0 (column wise)
    print(a.sum(axis=1))  # axis = 0 (row wise)
    b = a.sum(axis=0)
    print(b)
