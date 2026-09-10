'''
Input: int -> # of total steps
Output: int -> # of possible ways to achieve those steps
'''
"""
n = 0
output 1

n = 1
{1}
output: 1

n = 2 
{1,1}, {2}

ouput = 2 

n = 3
{1,1,1}{1,2}{2,1}
ouput = 3

n=4 
{1,1,1,1}{2,1,1}{1,1,2}{1,2,1}{2,2}
output = 5

n = 5
{1,1,1,1,1},{2,2,1}{2,1,2}{1,2,2}{1,1,2,1}{1,2,1,1}{2,1,1,1}{1,1,1,2}
output = 8


"""
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp 
        return one


        