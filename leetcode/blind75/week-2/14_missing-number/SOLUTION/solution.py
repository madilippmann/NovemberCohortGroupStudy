# Original source: https://github.com/neetcode-gh/leetcode/blob/main/268-Missing-Number.py

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])
        return res
