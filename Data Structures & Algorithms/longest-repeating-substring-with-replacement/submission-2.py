class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = dict()
        l = 0
        maxc = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            if ((r - l + 1) - max(count.values())) <= k:
                maxc = max(maxc, r - l + 1)
            else:
                while ((r - l + 1) - max(count.values())) > k:
                    count[s[l]] = count.get(s[l]) - 1
                    l += 1
        return maxc


        
        