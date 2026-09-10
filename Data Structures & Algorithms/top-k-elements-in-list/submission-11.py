class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Get a count of all elements create a dict (key is element, val is count of element) - Good

        Loop through the values of dict find largest return the key and - Good
        
        remove element from dict
        """
        count = dict()
        for num in nums:
            count[num] = count.get(num,0) + 1

        answer = []
        for i in range(k):
            maxVal = 0
            index = 0
            for key, value in count.items():
                maxVal = max(maxVal,value)
                if maxVal == value:
                    index = key

            answer.append(index)
            del count[index]
            

            
        return answer