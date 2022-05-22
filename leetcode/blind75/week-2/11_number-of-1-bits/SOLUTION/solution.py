# Original source: https://github.com/neetcode-gh/leetcode/blob/main/191-Number-of-1-Bits.py



class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= (n - 1)
            res += 1
        return res
