class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numsDict = dict()

        for i in range(len(numbers)):
            if target - numbers[i] in numsDict.keys():
                return [numsDict[target - numbers[i]] + 1, i + 1]
            numsDict[numbers[i]] = i