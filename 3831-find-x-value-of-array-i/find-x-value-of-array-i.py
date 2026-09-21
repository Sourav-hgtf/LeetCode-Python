class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            rem = num % k
            new_dp = [0] * k

            # Subarray containing only num
            new_dp[rem] = 1

            # Extend previous subarrays
            for r in range(k):
                new_rem = (r * rem) % k
                new_dp[new_rem] += dp[r]

            # Add current subarrays to answer
            for r in range(k):
                ans[r] += new_dp[r]

            dp = new_dp

        return ans