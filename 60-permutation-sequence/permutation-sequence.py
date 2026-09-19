class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]
        result = ""

        fact = 1
        for i in range(1, n):
            fact *= i

        k -= 1

        while n > 0:
            index = k // fact
            result += nums.pop(index)

            k %= fact
            n -= 1

            if n > 0:
                fact //= n

        return result