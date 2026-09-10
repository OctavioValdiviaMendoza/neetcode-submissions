class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S_len = len(s)
        T_len = len(t)
        if S_len != T_len:
            return False
        char_count = [0] * 26
        for i in range(S_len):
            char_count[ord(s[i]) - ord('a')] += 1 
        for i in range(T_len):
            char_count[ord(t[i]) - ord('a')] -= 1
        for num in char_count:
            if num != 0:
                return False
        return True
        