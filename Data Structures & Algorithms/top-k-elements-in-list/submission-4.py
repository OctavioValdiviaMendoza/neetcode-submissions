import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        heap = []
        answer = []
        
        for key,v in counter.items():
            heapq.heappush(heap, (-v,key))
        
        print(heap)
        
        for i in range(k):
            answer.append((heap.pop(0)[1]))
            heapq.heapify(heap)

            print(i, answer)

        return answer
