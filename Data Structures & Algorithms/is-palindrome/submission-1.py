"""
input: string that acn have nonAlphanumber characters
ouput: is a boolean that represents if it is a palindrome

#Filter the string of all non alphanumeric characters
#1.1.iterate throught the string from both start and end and compare character value at each point (to lower)
    1.1.2 If characters don't match Return False

return True
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = "".join(filter(str.isalnum,s))

        j = len(clean_string) - 1
        for i in range(len(clean_string)):
            if clean_string[i].lower() != clean_string[j].lower():
                return False
            j = j - 1

        return True
        