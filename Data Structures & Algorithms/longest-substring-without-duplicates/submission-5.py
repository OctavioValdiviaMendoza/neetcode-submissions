class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        visited = set()
        longest = 0
        for i in range(len(s)):
            while s[i] in visited:
                visited.remove(s[l])
                l += 1
            visited.add(s[i])
            longest = max(longest, i - l + 1)

        return longest