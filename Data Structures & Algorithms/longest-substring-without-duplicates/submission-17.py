class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        input: String
        Output: Int -> LongestSubstring without repeating characters


        two pointers one will be at the fron and one will be in adding to the dictionary
        As we find one in seen we want to use the pointer at the front to pop all the numbers from dict until it reahes the repeated char
        '''

        seen = dict()
        maxC = 0
        i, j = 0, 1
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        seen[s[i]] = i
        while j < len(s):
            if s[j] in seen:
                maxC = max(maxC, j - i)
                while s[i] != s[j]:
                    del seen[s[i]]
                    i += 1
                if s[i] == s[j]:
                    i += 1
                j += 1
            else:
                seen[s[j]] = j
                j += 1
        maxC = max(maxC, j-i)
        return maxC
            
            

            
            

            

        