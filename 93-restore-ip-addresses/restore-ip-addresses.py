class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def backtrack(index, parts):
            if len(parts) == 4:
                if index == len(s):
                    result.append(".".join(parts))
                return

            for length in range(1, 4):
                if index + length > len(s):
                    break

                part = s[index:index + length]

                # Leading zero is not allowed
                if len(part) > 1 and part[0] == '0':
                    continue

                # Value must be between 0 and 255
                if int(part) > 255:
                    continue

                parts.append(part)
                backtrack(index + length, parts)
                parts.pop()

        backtrack(0, [])

        return result