class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum_string = ""
        for char in s:
            if char.isalnum():
                alphanum_string += char.lower()
        
        stack = []
        for i in range(len(alphanum_string)//2):
            stack.append(alphanum_string[i])
        print(stack)
        if len(alphanum_string) % 2 == 0:
            start = len(alphanum_string) // 2
        else:
            start = len(alphanum_string) // 2 + 1
        for i in range(start, len(alphanum_string)):
                check_char = stack.pop()
                print(check_char)
                if alphanum_string[i] != check_char:
                    return False
        return True