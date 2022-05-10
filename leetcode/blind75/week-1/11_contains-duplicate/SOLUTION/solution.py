# Original Source: https://github.com/neetcode-gh/leetcode/blob/main/217-Contains-Duplicate.py

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
