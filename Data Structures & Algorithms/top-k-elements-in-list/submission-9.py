class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        if k == 0:
            return []
        count = dict()
        for num in nums:
            count[num] = count.get(num,0) + 1
        
        sortedCount = list(dict(sorted(count.items(), key=lambda item: item[1], reverse=True)))

        for i in range(0,k):
            answer.append(sortedCount[i])

        return answer


    

        
        
            

        
        