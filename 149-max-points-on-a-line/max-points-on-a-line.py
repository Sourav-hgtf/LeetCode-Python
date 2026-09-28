class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        if n <= 2:
            return n

        result = 1

        for i in range(n):
            slopes = {}

            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                if dx == 0:
                    key = (1, 0)
                elif dy == 0:
                    key = (0, 1)
                else:
                    if dx < 0:
                        dx = -dx
                        dy = -dy

                    g = math.gcd(abs(dx), abs(dy))
                    dx //= g
                    dy //= g

                    key = (dy, dx)

                slopes[key] = slopes.get(key, 0) + 1
                result = max(result, slopes[key] + 1)

        return result