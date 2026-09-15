class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        k = 0
        n = len(nums)
        ans = []
        for i in range(n * 2):
            if i < n:
                ans.append(nums[i])
            else:
                ans.append(nums[k])
                k +=1
        return ans
                

        