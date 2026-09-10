class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        input -> nums (int arr)
        output -> Boolean: (True-> Duplicate False -> No duplicate)
        '''

        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False
        