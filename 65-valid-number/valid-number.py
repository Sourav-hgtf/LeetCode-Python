class Solution:
    def isNumber(self, s: str) -> bool:
        i = 0
        n = len(s)

        if i < n and s[i] in "+-":
            i += 1

        digit = False
        dot = False

        while i < n and (s[i].isdigit() or s[i] == '.'):
            if s[i].isdigit():
                digit = True
            elif dot:
                return False
            else:
                dot = True
            i += 1

        if not digit:
            return False

        if i < n and s[i] in "eE":
            i += 1

            if i < n and s[i] in "+-":
                i += 1

            digit = False

            while i < n and s[i].isdigit():
                digit = True
                i += 1

            if not digit:
                return False

        return i == n