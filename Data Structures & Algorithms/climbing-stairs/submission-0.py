#Input is an integer
#Output is an integer of total possible

"""
    set a base case for 0 = 1 and 1=1 
    create a for loop that iterates from 0 to n

"""

"""
    1 = 1
    2 = [1+1] , [2]
    3 = [1+1+1], [2+1], [1+2]
    4 = [1+1+1+1], [2+2], [1+2+1], [2+1+1], [1+1+2]
    5 = [1+1+1+1+1], [2+2+1], [2+1+2], [1+2+2], [1+1+1+2], []
"""


class Solution:
    def climbStairs(self, n: int) -> int: 
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        prev2 = 1
        prev1 = 2
       
        for i in range(3, n+1):
            current = prev1+prev2
            prev2 =  prev1
            prev1 = current
        
        return prev1
        


        

        

        
        
        


        