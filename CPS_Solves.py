# https://leetcode.com/problems/binary-search/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        ans = -1

        while l <= r:
            mid = (l + r) // 2  # integer division

            if nums[mid] == target:
                ans = mid
                break
            else:
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1

        return ans
