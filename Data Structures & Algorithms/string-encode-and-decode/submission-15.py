class Solution:

    def encode(self, strs: List[str]) -> str:
        string_encoded = ""
        for string in strs:
            string_encoded += string
            string_encoded += "^^"
        return string_encoded


    def decode(self, s: str) -> List[str]:
        answer = s.split("^^")
        answer.pop()
        return answer


