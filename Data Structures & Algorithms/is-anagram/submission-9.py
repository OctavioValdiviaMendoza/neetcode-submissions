class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        string1 = dict()
        string2 = dict()
        for letter in s:
            string1[letter] =  1 + string1.get(letter, 0)
        for letter in t:
            string2[letter] = 1 + string2.get(letter, 0)
        return string1 == string2
