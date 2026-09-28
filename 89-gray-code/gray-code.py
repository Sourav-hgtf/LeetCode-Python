class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0]

        for i in range(n):
            value = 1 << i

            for j in range(len(result) - 1, -1, -1):
                result.append(result[j] + value)

        return result