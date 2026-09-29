class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in array:
                return [array[complement], i]

            array[nums[i]] = i
