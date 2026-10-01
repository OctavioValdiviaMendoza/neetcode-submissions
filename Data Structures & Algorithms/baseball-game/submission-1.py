class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = list()
        count = 0
        for opp in operations:
            if opp == "+":
                num1 = stack[-1]
                num2 = stack[-2]
                numSum = num1 + num2
                stack.append(numSum)
                count += numSum
            elif opp == "C":
                num = stack.pop()
                count -= num
            elif opp == "D":
                num1 = stack[-1]
                numDouble = num1 * 2
                stack.append(numDouble)
                count += numDouble
            else:
                stack.append(int(opp))
                count += int(opp)
        return count       