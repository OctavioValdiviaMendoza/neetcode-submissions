class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        '''
        iterate backwards to the arr, compare values to the right of it and if it is the max val replace it with current value

        '''
        original = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2, -1, -1):
            rightmax = max(original, arr[i+1])
            original = arr[i]
            arr[i] = rightmax
        return arr


        