class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min_val = None

    def push(self, val: int) -> None:
        if self.min_val == None:
            self.min_val = val
        else:
            self.min_val = min(self.min_val,val)

        self.stack.append([val, self.min_val])

        return None

    def pop(self) -> None:

        self.stack.pop()
        if not self.stack:
            self.min_val = None
        else:
            self.min_val = self.stack[-1][1]
        return None


    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.min_val