class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {']' : '[', ')' : '(', '}' : '{'}

        for char in s:
            if char in closeToOpen:
                if not stack or closeToOpen[char] != stack.pop():
                    return False
            else:
                stack.append(char)
        return True if not stack else False


        