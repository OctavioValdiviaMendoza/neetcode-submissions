class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_of_nums = set()
        max_c = 0
        for num in nums:
            set_of_nums.add(num)
        
        for num in nums:
            if num - 1 not in set_of_nums:
                length = 0
                while (num + length) in set_of_nums:
                    length += 1
                max_c = max(length, max_c)
        return max_c



        

        return 0
        