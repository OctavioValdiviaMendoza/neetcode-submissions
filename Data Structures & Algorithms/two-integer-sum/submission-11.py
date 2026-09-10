class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        potentialAnswer = set()
        answer = [0,0]
        for number in nums:
            potentialAnswer.add(target-number)  
        for i in range(0, len(nums)):
            if nums[i] in potentialAnswer:
                answer[1] = i
        for i in range(0, len(nums)):
            if nums[i] == (target - nums[answer[1]]):
                answer[0] = i 
                return answer
       


            


            
        