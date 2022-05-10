# Original Source: https://github.com/neetcode-gh/leetcode/blob/main/20-Valid-Parentheses.py

class Solution:
    def isValid(self, s: str) -> bool:
        Map = { ")":"(", "]":"[", "}":"{" }
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack
