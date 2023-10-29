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
l = int(input())
a = int(input())
p = int(input())
ct = 0
f = 1
total = 0
maxim = 0
while(f):
    ct+=1
    lemon = 1*ct
    apple = 2*ct
    pear = 4*ct

    if lemon<=l and apple<=a and pear<=p:
        total = lemon+apple+pear
        maxim = max(total,maxim)
    else:
        f = 0

print(maxim)