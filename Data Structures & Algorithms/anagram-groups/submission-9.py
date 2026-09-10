class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        for string in strs:
            anagrams.setdefault("".join(sorted(string)),[]).append(string)

        return list(anagrams.values())
        
