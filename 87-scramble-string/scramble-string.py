class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        cache = {}

        def solve(a, b):
            if (a, b) in cache:
                return cache[(a, b)]

            if a == b:
                return True

            if len(a) != len(b):
                return False

            if sorted(a) != sorted(b):
                cache[(a, b)] = False
                return False

            n = len(a)

            for i in range(1, n):
                # No swap
                if solve(a[:i], b[:i]) and solve(a[i:], b[i:]):
                    cache[(a, b)] = True
                    return True

                # Swap
                if solve(a[:i], b[n-i:]) and solve(a[i:], b[:n-i]):
                    cache[(a, b)] = True
                    return True

            cache[(a, b)] = False
            return False

        return solve(s1, s2)