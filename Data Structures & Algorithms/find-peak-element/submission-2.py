class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        Iterate through nums, haev if conditoin for first element and have if conditon for last element check if they are always larger than their neighbor sis true 

        '''
        if len(nums) == 1:
            return 0

        for i in range(len(nums)):
            if i == 0:
                if nums[i] > nums[i + 1]:
                    return i
            elif i == (len(nums) - 1):
                if nums[i] > nums[i - 1]:
                    return i
            else:
                if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                    return i
        
