class MinStack:

    '''
    -202
    -2-2-2
    '''

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min_stack.append(val)
        else:
            min_val = self.min_stack[-1]
            min_val = min(min_val, val)
            self.min_stack.append(min_val)
        return self.stack.append(val)

    def pop(self) -> None:
        self.min_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
