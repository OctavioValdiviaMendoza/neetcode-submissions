class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        n = len(s)
        if n % 2 == 1:
            return False
        
        stack = []
        for par in s:
            if par == '[':
                stack.append(']')
            elif par == '(':
                stack.append(')')
            elif par == '{':
                stack.append('}')
            else:
                if len(stack) == 0:
                    return False
                comp_par = stack.pop()
                if comp_par != par:
                    return False
        if len(stack) != 0:
            return False
        return True




        