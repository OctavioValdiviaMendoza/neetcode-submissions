class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = dict()
        countT = dict()

        for char in s:
            countS[char] = countS.get(char, 0) + 1;

        for char in t:
            countT[char] = countT.get(char, 0) + 1;

        return countT == countS

        