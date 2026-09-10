class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size_of_nums = len(nums)
        answer = [1] * size_of_nums

        #Creates anwer array for num prev nums
        for i in range (1, size_of_nums):
            answer[i] =  answer[i-1] * nums[i - 1]
        
        print(answer)
        #Creates answer array for post nums
        for i in range (size_of_nums - 2 , -1, -1):
            nums[i] = nums[i] * nums[i + 1]
        
        print(nums)

        for i in range (size_of_nums - 2, -1 , -1):
            answer[i] = answer[i] * nums[i + 1]
        
        return answer
            




        
