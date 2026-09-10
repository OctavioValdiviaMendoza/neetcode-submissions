class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        string1 = dict()
        string2 = dict()
        for letter in s:
            if letter in string1:
                string1[letter] += 1
            else:
                string1[letter] = 0
        for letter in t:
            if letter in string2:
                string2[letter] += 1
            else:
                string2[letter] = 0
        return string1 == string2
