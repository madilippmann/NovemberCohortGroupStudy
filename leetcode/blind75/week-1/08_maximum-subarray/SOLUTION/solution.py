# Original Source: https://github.com/neetcode-gh/leetcode/blob/main/53-Maximum-Subarray.py

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]

        total = 0
        for n in nums:
            total += n
            res = max(res, total)
            if total < 0:
                total = 0
        return res
