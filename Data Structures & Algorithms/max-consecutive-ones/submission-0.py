class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max_c = 0
        for num in nums:
            if num == 1:
                counter += 1
                max_c = max(counter, max_c)
            else:
                counter = 0
        
        return max_c
        