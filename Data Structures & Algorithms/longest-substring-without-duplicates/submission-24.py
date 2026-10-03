class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        set -> elements traversed in window
        two pointer/ sliding window:
       
        l r , increase right pointer (adding to legnth var, checking curr max len) until I find a repeated char
        
        remove elemtns from set until left pointer reaches the repeated char continue expanding the right pointer
        '''
        window = set()
        longest_sub_sequence = 0
        current_sub_sequence = 0 

        l = 0


        for r in range(len(s)):
            if s[r] not in window:
                window.add(s[r])
                current_sub_sequence += 1
                longest_sub_sequence = max(longest_sub_sequence, current_sub_sequence)
            else:
                while s[l] != s[r]:
                    window.remove(s[l])
                    l += 1
                    current_sub_sequence -= 1
                l +=1        
        return longest_sub_sequence
                

