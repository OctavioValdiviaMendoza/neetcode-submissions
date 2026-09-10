class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        answer = set()
        for i in nums:
            if i in answer:
                return True
            answer.add(i)
        return False