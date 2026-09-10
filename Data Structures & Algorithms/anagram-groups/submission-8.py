class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        res = []
        for string in strs:
            anagrams.setdefault("".join(sorted(string)),[]).append(string)
        for val in anagrams.values():
            res.append(val)

        return res
        
