class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       pastEl = {}

       for i, num in enumerate(nums):
            if target - num in pastEl:
                return [pastEl[target-num], i]
            pastEl[num] = i 