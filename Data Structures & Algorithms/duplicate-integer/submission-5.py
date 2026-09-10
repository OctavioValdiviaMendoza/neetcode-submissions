"""
input: list that contains integers
output: Boolean -> there is a duplicate integere in the list given (if yes -> true) (if not -> False)

List can be empty -> False 

To make a dic: key -> int and value: # of occurences of int
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        answer = dict()
        for num in nums:
            answer[num] = 1 + answer.get(num, 0)

        for values in answer.values():
            if values > 1:
                return True
        
        return False