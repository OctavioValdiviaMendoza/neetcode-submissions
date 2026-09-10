class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Create a dictionary with key [2] = # of occurences
        # Create an array called asnwer = []
        # iterate through find max  from all the values append to the key answer list set value to 0 
        #for that key

        count = dict()
        answer = []
        temp = 0

        for num in nums:
            count[num] = count.get(num , 0) + 1
        
        print(count)
        
        for i in range(k):
            print(i)
            for key,value in count.items():
                temp = max(temp, value)
            print(temp)
            for key,value in count.items():
                if value == temp:
                    answer.append(key)
                    temp = 0
                    count[key] = 0
                    break

        
        return answer
        
            

