from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []

        def solve(string, open_count, close_count):

            if len(string) == 2 * n:
                result.append(string)
                return

            if open_count < n:
                solve(string + "(", open_count + 1, close_count)

            if close_count < open_count:
                solve(string + ")", open_count, close_count + 1)

        solve("", 0, 0)

        return result