class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "empty"
        final_string = ""
        if len(strs) == 1 and strs[0] == "":
            return final_string

        for i in range (0, len(strs)):
            if i != len(strs) - 1:
                final_string += strs[i] + "___"
            else:
                final_string += strs[i]
        
        return final_string

    def decode(self, s: str) -> List[str]:
        print(s)
        if s == "empty":
            return []
        elif s == "":
            return [""]
        final_arr = s.split("___")
        return final_arr