class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lenS = len(s)
        if lenS == 0:
            return 0
        if lenS == 1:
            return 1
        l,r = 0, 1
        seen = set()
        seen.add(s[l])
        maxS = 0
        while r < lenS:
            if s[r] in seen:
                maxS = max(maxS, r-l)
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                l +=1
            seen.add(s[r])
            r +=1
            maxS = max(maxS,r-l)
        return maxS

                



        