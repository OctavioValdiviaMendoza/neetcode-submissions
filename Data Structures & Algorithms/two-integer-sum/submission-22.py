class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        array of int -> find i and j such that nums[i] + nums[j] == target and i !=j
        Dict(key -> num in nums arr, val-> index)
        target - i in dict

        '''
        numsDict = dict()
        for i in range(len(nums)):
            j = target - nums[i]
            if j in numsDict.keys():
                return[numsDict[j], i]
            numsDict[nums[i]] = i

        