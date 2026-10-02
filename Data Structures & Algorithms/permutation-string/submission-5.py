class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        countS1 = dict()
        #count S1 chars
        for char in s1:
            countS1[char] = countS1.get(char,0) + 1 

        
        countS2 = dict()
        l = 0
        for r in range(len(s2)):
            if s2[r] in countS1.keys():
                countS2[s2[r]] = countS2.get(s2[r], 0) +  1
                if countS2.get(s2[r], 0) > countS1.get(s2[r], 0):
                    while(s2[l] != s2[r]):
                        countS2[s2[l]] = countS2.get(s2[l]) - 1
                        l += 1
                    countS2[s2[l]] = countS2.get(s2[l]) - 1
                    l += 1
            else:
                countS2 = dict()
                l = r + 1  
            
            
            if countS1 == countS2:
                return True


        return False 

        