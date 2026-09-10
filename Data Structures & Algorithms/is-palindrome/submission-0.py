class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ''.join(filter(str.isalnum,s))
        print(s2)
        j = len(s2) - 1
        for i in range (0, len(s2)):
            if s2[i].lower() != s2[j].lower():
                return False
            j = j - 1
        return True
