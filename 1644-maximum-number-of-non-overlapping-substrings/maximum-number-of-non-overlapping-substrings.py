class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        first = [len(s)] * 26
        last = [-1] * 26

        for i in range(len(s)):
            x = ord(s[i]) - ord('a')
            first[x] = min(first[x], i)
            last[x] = i

        intervals = []

        for c in range(26):
            if last[c] == -1:
                continue

            left = first[c]
            right = last[c]
            i = left
            valid = True

            while i <= right:
                x = ord(s[i]) - ord('a')

                if first[x] < left:
                    valid = False
                    break

                right = max(right, last[x])
                i += 1

            if valid:
                intervals.append([left, right])

        intervals.sort(key=lambda x: x[1])

        result = []
        end = -1

        for left, right in intervals:
            if left > end:
                result.append(s[left:right + 1])
                end = right

        return result