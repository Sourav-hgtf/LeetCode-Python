class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break

                path.append(candidates[i])
                backtrack(i, target - candidates[i], path)
                path.pop()

        candidates.sort()
        backtrack(0, target, [])
        return result