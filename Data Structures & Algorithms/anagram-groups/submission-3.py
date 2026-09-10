class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        if len(strs) == 0:
            return [[""]]

        """
        inside first for loop create dictionary containing the the key being the letter and value being the amount it appears

        second foorloop creates a dictionary for the first string that appears in each sub list in asnwers array

        compare the strings if anagramms append to list if not append to asnwer list (parent list)
        """
        answer = []

        for string in strs:
            if len(answer) == 0:
                answer.append([string])
                continue
            dict1 = {}
            changed = False
            #makes dictionary [char: instances]
            for char in string:
                if char in dict1:
                    dict1[char] += 1
                else:
                    dict1[char] = 1
            print(dict1)
            for i in range (0, len(answer)):
                stringInList = answer[i][0]
                if len(string) != len(stringInList):
                    continue    
                else:
                    print("WE MADE IT")
                    print(dict1)
                    dict2 = {}
                    for char in stringInList:
                        if char in dict2:
                            dict2[char] += 1
                        else:
                            dict2[char] = 1
                    print(dict2)
                    if dict1 == dict2 and changed != True:
                        answer[i].append(string)
                        changed = True
            if changed == False:
                answer.append([string])
            print(answer)

        return answer

            

