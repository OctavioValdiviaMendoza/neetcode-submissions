class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Create a Hash Map/Dictonary:
        key -> val in nums
        value -> index in nums
        """
        numsHashMap = dict()
        for i in range(len(nums)):
            numsHashMap[nums[i]] = i
        
        for i in range(len(nums)):
            if target - nums[i] in numsHashMap.keys() and i != numsHashMap[target - nums[i]]:
                return[i, numsHashMap[target - nums[i]]]
