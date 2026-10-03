class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        return arr ->[i,j] where nums[i] + nums[j] == target

        Approach:
        Dictionary -> key being #, value -> index

        for i in range(len(nums)):
            check target - nums[i] in Dictionary
                return [Dictionary[target - nums[i], i]
            else:
                add the curr element to Dictionary

        '''

        refrence = dict()
        for i in range(len(nums)):
            if target - nums[i] in refrence.keys():
                return [refrence[target - nums[i]], i]
            refrence[nums[i]] = i
        return 0 
        