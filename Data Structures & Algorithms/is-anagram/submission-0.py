class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        answer = {}
        for char in s:
            if char in answer:
                answer[char] = answer[char] + 1
            else:
                answer[char] = 1
        print(answer)
        for char in t:
            if char in answer:
                answer[char] = answer[char] - 1
            else:
                return False
        print(answer)
        for value in answer.values():
            if value != 0:
                return False
        return True
        