class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack != []:
            self.stack.insert(0, [val, min(val, self.stack[0][1])])
        else:
            self.stack.insert(0, [val, val])
        
    def pop(self) -> None:
        self.stack.pop(0)
    def top(self) -> int:
        return self.stack[0][0]

    def getMin(self) -> int:
        return self.stack[0][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
