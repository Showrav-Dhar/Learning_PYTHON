# https://leetcode.com/problems/binary-search/
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         l = 0
#         r = len(nums) - 1
#         ans = -1
#
#         while l <= r:
#             mid = (l + r) // 2  # integer division
#
#             if nums[mid] == target:
#                 ans = mid
#                 break
#             else:
#                 if nums[mid] > target:
#                     r = mid - 1
#                 else:
#                     l = mid + 1
#
#         return ans

# n = int(input())
# line = input()
# li = []
# ct = 1
# for i in range(1, n):
#     if line[i] == 'x' and line[i - 1] == 'x':
#         ct += 1
#         if ct == 3:
#             li.append(line[i])
#             ct = 2
#     else:
#         ct = 1
#
#     sz = len(li)
# print(sz)

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     st = input()
#     ans = 1
#     temp = 1
#     for i in range(1, n):
#         if st[i] == st[i - 1]:
#             temp = temp + 1
#         else:
#             ans = max(ans, temp)
#             temp = 1
#
#     ans = max(ans, temp)
#
#     print(ans + 1)
#
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     st = input()
#     Lpos = -1
#     Rpos = -1
#     for i in range(n - 1, -1,-1):
#         if st[i] == 'L':
#             Lpos = i + 1
#             break
#
#     for i in range(n):
#         if st[i] == 'R':
#             Rpos = i + 1
#             break
#
#     if Lpos == -1 or Rpos == -1:
#         print(-1)
#     elif Lpos > Rpos:
#         print(0)
#     else:
#         if Lpos < Rpos:
#             Lpos = Lpos - 1
#             if st[Lpos] == 'R':
#                 print(Lpos + 1)
#             else:
#                 print(-1)
#         else:
#             print(-1)
# l = int(input())
# a = int(input())
# p = int(input())
# ct = 0
# f = 1
# total = 0
# maxim = 0
# while(f):
#     ct+=1
#     lemon = 1*ct
#     apple = 2*ct
#     pear = 4*ct
#
#     if lemon<=l and apple<=a and pear<=p:
#         total = lemon+apple+pear
#         maxim = max(total,maxim)
#     else:
#         f = 0
#
# print(maxim)

#
# import collections
#
# if __name__ == '__main__':
#     n, k = map(int, input().split())
#     ara = list(map(int, input().split()))
#
#     dq = collections.deque()
#     freq = collections.defaultdict()
#
#     for a in ara:
#         if len(dq) == 0:
#             dq.appendleft(a)
#             freq[a] = freq.get(a, 0) + 1
#         else:
#             if a not in freq:
#                 if len(dq) >= k:
#                     b = dq.pop()
#                     del freq[b]
#
#                     dq.appendleft(a)
#                     freq[a] = freq.get(a, 0) + 1
#                 else:
#                     dq.appendleft(a)
#                     freq[a] = freq.get(a, 0) + 1
#
#     print(len(dq))
#     print(*dq)
#
# n = int(input())
# li1 = list(map(int, input().split()))
# q = int(input())
# li2 = list(map(int, input().split()))
#
# li1.sort()
# li2.sort()
#
# ct = 0
# prev = -1
# for i in li1:
#     if prev == i:
#         continue
#     else:
#         prev = i
#
#     isPresent = False
#
#     l = 0
#     r = q - 1
#
#     while l <= r:
#         m = int((l + r) / 2)
#
#         if li2[m] == prev:
#             isPresent = True
#             break
#         elif li2[m] > prev:
#             r = m - 1
#         else:
#             l = m + 1
#
#     if isPresent:
#         ct += 1
#
# print(ct)

#
# t = int(input())
# for p in range(t):
#     st = input()
#
#     ans = 1
#     if st[0] == '0':
#         ans = 0
#     elif st[0] != '0' and st[0] != '?':
#         ans = 1
#     else:
#         ans = 9
#
#     n = len(st)
#     for i in range(1, n):
#         if st[i] == '?':
#             ans = ans * 10
#
#     print(ans)


# https://www.spoj.com/problems/MATHLOVE/en/

# def getvalue(n):
#     return n * (n + 1) // 2
#
#
# t = int(input())
# for test in range(t):
#     a = int(input())
#
#     l = 1
#     r = a
#     ans = -1
#     while l <= r:
#         mid = (l + r) // 2
#
#         if getvalue(mid) == a:
#             ans = mid
#             break
#         elif getvalue(mid) > a:
#             r = mid - 1
#         else:
#             l = mid + 1
#
#     if ans == -1:
#         print("NAI")
#     else:
#         print(int(ans))


# https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/monks-encounter-with-polynomial/?purpose=login&source=problem-page&update=google

# t = int(input())
# for _ in range(t):
#     a, b, c, k = map(int, input().split())
#
#     l = 0
#     r = 1e5
#     pos = r + 1
#
#     while l <= r:
#         mid = (l + r) // 2  # integer division
#         ans = a*(mid * mid) + (b * mid) + c
#
#         if ans >= k:
#             r = mid - 1
#             pos = min(mid, pos)
#         else:
#             l = mid + 1
#
#     print(int(pos))

# random cf
t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(1, end= " ")
    else:
        if n % 2 != 0:
            print(-1,end= " ")
        else:
            for i in range(1, n + 1):
                if i % 2 == 1:
                    print(i+1, end=" ")
                else:
                    print(i-1, end=" ")
    print()