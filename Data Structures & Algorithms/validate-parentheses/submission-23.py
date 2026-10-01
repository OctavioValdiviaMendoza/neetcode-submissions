class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) % 2 == 1:
            return False
        stack = list()
        for char in s:
            if char == "(":
                stack.append(")")
            elif char == "[":
                stack.append("]")
            elif char == "{":
                stack.append("}")
            else:
                if len(stack) == 0:
                    return False
                val = stack.pop()
                if char != val:
                    return False
        if len(stack) != 0:
            return False
        return True

        