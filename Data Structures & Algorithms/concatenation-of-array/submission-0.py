class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        '''
        1,2,3
        1,2,3,1,2,3

        '''
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
                

        