class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        answer = set()
        for number in nums:
            if number not in answer:
                answer.add(number)
            else:
                return True
        return False