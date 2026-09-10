class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        input: -> nums arr
        output: ->List[list[nums]]

        iterate through arr:
            for num in nums 

        dict = (key -> value in nums, value-> index in nums)
        
        the do the 2 sum method in the remaining part of array
        with target being dynamic


        [x, y, z]

        '''
        res = set()
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            seen = {}
            for j in range(i + 1, len(nums)):
                potential = -(nums[i]+ nums[j])
                if potential in seen:
                    res.add((nums[i],nums[j], potential))
                else:
                    seen[nums[j]] = j
        
        return [list(triplet) for triplet in res]
                    

            

            
        