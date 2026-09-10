class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        Given: arr of int

        Return True if apperance > 1 else False
        '''

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        