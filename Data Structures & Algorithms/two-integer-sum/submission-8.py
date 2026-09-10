class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = [0,0]
        for i in range(len(nums) - 1,-1,-1):
            if (target - nums[i]) in nums :
                answer[1] = nums[i]
                answer[0] = target - nums[i]
                break
        print(answer)
        answer[0] = nums.index(answer[0])
        for i in range(answer[0] + 1, len(nums)):
            if nums[i] == answer[1]:
                print("true")
                answer[1] = i
                break
        
        return answer