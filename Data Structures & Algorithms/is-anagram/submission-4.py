class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic1 = {}
        dic2 = {}
        for char1, char2 in zip(s,t):
            if char1 in dic1:
                dic1[char1] += 1
            else:
                dic1[char1] = 1
            if char2 in dic2:
                dic2[char2] += 1
            else:
                dic2[char2] = 1
        if dic1 == dic2:
            return True
        return False
        