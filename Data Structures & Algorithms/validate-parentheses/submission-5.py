"""
Input: string consisiting of brackets
Ouput: Boolean depending of if brackets match (open/close)

1. Check if string len is even
2. Then I would iterate through the string and compare values of each end to see if they match
    2.2 IF they don't return False
    2.3 else return true
"""

class Solution:
    def isValid(self, s: str) -> bool:
        s_len = len(s)

        if s_len % 2 != 0:
            return False
        j = s_len - 1

        close_brackets = {']','}',')'}

        stack = []


        for i in range(s_len):
            if s[i] == '{':
                stack.insert(0,'}')
            if s[i] == '[':
                stack.insert(0,']')
            if s[i] == '(':
                stack.insert(0,')')
            if s[i] in close_brackets:
                if len(stack) > 0:
                    temp = stack.pop(0)
                    if s[i] != temp:
                        return False
                else:
                    return False
            
        if stack != []:
            return False
        
        return True
        
        