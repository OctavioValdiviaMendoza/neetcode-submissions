class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        total_value_of_arr = num
               x
        [1,7,3,6,5,6]

        current_value = sum of all number until the ith position 
        left_over = (current_value + current_index) - total_value

        if current_value == left_over
            return current index
        '''
        total_value_of_arr = 0
        current_value = 0
        for num in nums:
            total_value_of_arr += num

        for i in range(len(nums)):
            if i == 0:
                current_value = 0
            else:
                current_value += nums[i-1]
            left_over = total_value_of_arr-(current_value + nums[i])
            if current_value == left_over:
                return i
        return -1

        
        

        