class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        dictionary[sorted.word, array]

        iterate through dict and return list of result
        """

        if not strs:
            return []
        if len(strs) == 1:
            return [strs]
        anagramDict = dict()
        for string in strs:
            anagramDict.setdefault("".join(sorted(string)), []).append(string)
        
        result = []
        for value in anagramDict.values():
            result.append(value)

        return result



        

        