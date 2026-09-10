class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 0:
            return True
        if len(s) % 2 != 0:
            return False
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(')')
            elif s[i] == '{':
                stack.append('}')
            elif s[i] == '[':
                stack.append(']')
            else:
                if not stack:
                    return False
                closing_bracket = stack.pop()
                if s[i] != closing_bracket:
                    return False
        
        return len(stack) == 0


                