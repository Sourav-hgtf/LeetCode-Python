class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            value = ord(s[i]) - ord('a') + 1
            reverse_value = 27 - value
            result += reverse_value * (i + 1)

        return result