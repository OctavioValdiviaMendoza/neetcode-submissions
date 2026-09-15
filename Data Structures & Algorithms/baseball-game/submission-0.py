class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        count = 0
        for i in range(len(operations)):
            if operations[i] == "+":
                sum_score = stack[-1] + stack[-2]
                stack.append(sum_score)
            elif operations[i] == "C":
                stack.pop()
            elif operations[i] == "D":
                num_doubled = stack[-1] * 2
                stack.append(num_doubled)
            else:
                stack.append(int(operations[i]))

        for num in stack:
            count += num
        return count
