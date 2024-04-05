#   BASIC DATA TYPES SECTION ON HackerRANK
# import numpy


# Find the Runner-Up Score!

# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#
#
#     l1 = list(set(arr))
#     len1 = len(l1)
#     l1.sort()
#     print(l1[len1-2])

# LISTS
#
# N = int(input())
# ans_l = []
# for i in range(N):
#     l1 = input().split(' ')
#
#     if len(l1) == 1:
#         if l1[0] == "sort":
#             ans_l.sort()
#         elif l1[0] == "pop":
#             ans_l.pop(-1)
#         elif l1[0] == "reverse":
#             ans_l.reverse()
#         elif l1[0] == "print":
#             print(ans_l)
#     elif len(l1) == 2:
#         if l1[0] == "append":
#             ans_l.append(int(l1[1]))
#         elif l1[0] == "remove":
#             ans_l.remove(int(l1[1]))
#     elif len(l1) == 3:
#         if l1[0] == "insert":
#             ans_l.insert(int(l1[1]), int(l1[2]))
#
# TUPLES
# if name == 'main':
#     n = int(input())
#     integer_list = map(int, input().split())
#     print
#     (hash(tuple(integer_list)))


# def swap_case(s):
#     str = ''
#     for i in s:
#         if i.islower():
#             str += i.upper()
#         # print(i.upper(),end='')
#         elif i.isupper():
#             str += i.lower()
#         # print(i.lower(),end='')
#         else:
#             str += i
#         # print(i,end='')
#     return str
#
# s = input()
# ans = swap_case(s)
# print(ans)


# occurence of a substring in a string using python
# def count_substring(string, sub_string):
#     count = 0
#     start = 0
#
#     while start<len(string):
#
#         pos = string.find(sub_string,start)
#
#         if pos!=-1:
#             start = pos+1
#             count+=1
#         else:
#             break
#
#
#     return count
#
# print(count_substring("ABCDCDC","CDC"))
#
# if __name__ == '__main__':
#     t = int(input())
#     for tc in range(t):
#         n = int(input())
#         ara = list(map(int, input().split()))
#         ara.sort()
#         mx = ara[n - 1]
#         ct = ara.count(mx)
#
#         if ct == n:
#             print("-1")
#         else:
#             print(f"{n - ct} {ct}")
#             for i in range(0,n - ct):
#                 print(ara[i], end=' ')
#             print('\n')
#             for i in range(n - ct, n):
#                 print(ara[i], end=' ')
#             print('\n')

# def fact(n):
#     if n == 1:
#         return 1
#
#     return (n*fact(n-1))
#
#
# if __name__ == '__main__':
#     t = int(input())
#     for a in range(t):
#         x = int(input())
#         print(fact(x))


# factorial using dp
# import sys
#
# sys.setrecursionlimit(10 ** 6 + 5)
#
# dp = [-1] * (10 ** 6 + 123)
#
#
# def fact(n):
#     if n == 1:
#         return 1
#     if dp[n] != -1:
#         return dp[n]
#
#     dp[n] = n * (fact(n - 1)) % 1000000007
#
#     return dp[n]
#
#
# if __name__ == '__main__':
#
#     t = int(input())
#     for x in range(t):
#         a = int(input())
#         print(fact(a))

#
# import numpy as np
#
# if __name__ == '__main__':
#     a = list(map(int, input().split()))
#     mat = np.array(a)
#     # mat.shape = (3,3)
#     # print(mat)
#     print(numpy.reshape(mat, (3, 3)))

# import numpy as np
#
# if __name__ == '__main__':
#     n, m = map(int, input().split())
#     li = []
#
#     for i in range(n):
#         l1 = list(map(int, input().split()))
#         li.append(l1)
#
#     a = np.array(li)
#     a.shape = (n, m)
#     b = np.transpose(a)
#     print(b)
#     print(b.flatten('F'))

#
# import numpy as np
#
# if __name__ == '__main__':
#     n, m, p = map(int, input().split())
#     li1 = []
#     for i in range(n):
#         l1 = list(map(int, input().split()))
#         li1.append(l1)
#
#     li2 = []
#     for i in range(m):
#         l2 = list(map(int, input().split()))
#         li2.append(l2)
#
#     a = np.array(li1)
#     b = np.array(li2)
#     li1.clear()
#     li2.clear()
#     a.shape = (n, p)
#     b.shape = (m, p)
#
#     print(np.concatenate((a, b), axis=0))
#
# import numpy as np
#
# if __name__ == '__main__':
#     l1 = list(map(int,input().split()))
#     print(np.zeros(l1, dtype=int))
#     print(np.ones(l1, dtype=int))

# import numpy as np
#
# if __name__ == '__main__':
#     n, m = map(int, input().split())
#     l1 = []
#     for i in range(n):
#             l = list(map(int, input().split()))
#             l1.append(l)
#
#     a1 = np.array(l1)
#     a1.shape = (n, m)
#
#     l2 = []
#     for i in range(n):
#             l = list(map(int, input().split()))
#             l2.append(l)
#
#     a2 = np.array(l2)
#     a2.shape = (n, m)
#
#     print(np.add(a1, a2))
#     print(np.subtract(a1, a2))
#     print(np.multiply(a1, a2))
#     print(np.floor_divide(a1, a2))
#     print(np.mod(a1, a2))
#     print(np.power(a1, a2))

# import numpy as np
# np.set_printoptions(legacy='1.13')
#
#
# n, m = map(int, input().split())
# print(np.eye(n, m, k=0))

# import numpy as np
# np.set_printoptions(legacy='1.13')
#
# if __name__ == '__main__':
#
#     l1 = list(map(float,input().split()))
#     a = np.array(l1)
#     print(np.floor(a))
#     print(np.ceil(a))
#     print(np.rint(a))
#

# working with linear algebra functions

# import numpy as np
#
# if __name__ == '__main__':
#     n = int(input())
#     l1 = []
#     for i in range(n):
#         l = list(map(float, input().split()))
#         l1.append(l)
#
#     ara = np.array(l1)
#
#     print(round(np.linalg.det(ara),2))
#
# import numpy as np
# if __name__ == '__main__':
#     n,m = map(int,input().split())
#     li = []
#     for i in range (n):
#         l1 = list(map(float,input().split()))
#         li.append(l1)
#
#     ara = np.array(li)
#
#     print(np.mean(ara,axis=1))
#     print(np.var(ara,axis=0))
#     print(round( np.std(ara,axis=None) , 11 ))


# import numpy as np
# if __name__ == '__main__':
#     n,m = map(int,input().split())
#     li = []
#     for i in range(n):
#         l1 = list(map(int,input().split()))
#         li.append(l1)
#
#     a = np.array(li)
#
#     print(np.prod(np.sum(a,axis=0)))
#
# import heapq
#
# def all_possible_pair(array):
#   """
#   Generates all possible pairs from an array in O(n log n) time.
#
#   Args:
#     array: A list of elements.
#
#   Returns:
#     A list of all possible pairs from the array.
#   """
#
#   heapq.heapify(array)
#   result = []
#   while len(array) > 1:
#     smallest = heapq.heappop(array)
#     largest = heapq.heappop(array)
#     result.append((smallest, largest))
#     heapq.heappush(array, smallest)
#   return result
#
# array = [1, 2, 3, 4, 5]
# print(all_possible_pair(array))

# if __name__ == '__main__':
#     a = int(input())
#     li = list(map(int, input().split()))
#     dic = {}
#     for i in range(a):
#         dic[li[i]] = dic.get(li[i], 0) + 1
#
#     li2 = []
#     for i in range(a-1, -1, -1):
#         x = li[i]
#         if dic[x] != -1:
#             li2.append(x)
#             dic[x] = -1
#
#     print(len(dic))
#     li2.reverse()
#     print(*li2)

#
# n, k = map(int, input().split())
# vec = list(map(int, input().split()))
# ara = {}
# for i in range(n):
#     a = vec[i]
#     vec.append(a)
#     if a in ara:
#         ara[a] += 1
#     else:
#         ara[a] = 1
#
# vec.sort()
# f = set()
# for i in range(n):
#     x = vec[i]
#     ct = 0
#     for key, value in ara.items():
#         if key <= x:
#             ct += value
#     f.add((x, ct))
#
# ans = -1
# for x, ct in f:
#     if ct == k:
#         ans = x
#         break
#
# print(ans)
#
# t = int(input())
# for p in range(0,t):
#     n, k, x = map(int, input().split())
#     if k > min(n, x + 1):
#         print(-1)
#     else:
#         sum = 0
#         for i in range(0, k):
#             sum += i
#             n = n - 1;
#
#         if k == x:
#             for i in range(0,n):
#                 sum += (x - 1)
#         else:
#             for i in range(0,n):
#                 sum += x
#
#         print(sum)

t = int(input())
for tc in range(t):
    n = int(input())
    st = input()
    st1 = "map"
    st2 = "pie"
    ct1 = st.count(st1)
    ct2 = st.count(st2)
    # print(ct1,ct2)
    p_assumed = (ct1 + ct2)
    p_have = st.count('p')
    if ct1 != 0 or ct2 != 0:
        print((p_assumed-p_have))
    else:
        print(0)
