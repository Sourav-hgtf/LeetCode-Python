class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        have = {}
        left = 0
        count = 0

        best_start = 0
        best_length = float('inf')

        for right in range(len(s)):
            ch = s[right]
            have[ch] = have.get(ch, 0) + 1

            if ch in need and have[ch] <= need[ch]:
                count += 1

            while count == len(t):
                if right - left + 1 < best_length:
                    best_length = right - left + 1
                    best_start = left

                left_ch = s[left]
                have[left_ch] -= 1

                if left_ch in need and have[left_ch] < need[left_ch]:
                    count -= 1

                left += 1

        if best_length == float('inf'):
            return ""

        return s[best_start:best_start + best_length]