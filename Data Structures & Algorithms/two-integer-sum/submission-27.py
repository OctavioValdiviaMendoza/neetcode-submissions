class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #(Key: value in array, Value: index of value)
        nums_dict = dict()
        for index, num in enumerate(nums):
            if target - nums[index] in nums_dict and index != nums_dict[target - nums[index]]:
                return[nums_dict[target - nums[index]], index]
            nums_dict[num] = index
        return 0 



        