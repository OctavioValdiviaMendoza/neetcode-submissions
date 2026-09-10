class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        answer = []
        for i in nums:
            if i in answer:
                return True
            else:
                answer.append(i)
        return False