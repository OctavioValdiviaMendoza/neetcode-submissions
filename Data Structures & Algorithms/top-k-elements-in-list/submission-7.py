class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        arr = [[] for i in range(len(nums) + 1)]
        answer = []

        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        for key, val in count.items():
             arr[val].append(key)
        
        print(arr)

        for i in range (len(arr) -1, 0, -1):
            for n in arr[i]:
                answer.append(n)
                if len(answer) == k:
                    return answer
            
        


            


        