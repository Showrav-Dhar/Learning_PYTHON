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
