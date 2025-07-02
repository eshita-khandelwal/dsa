class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            a,b = self.stack[-1]
            self.stack.append([val,min(val,b)])
        else:
            self.stack.append([val,min(val,val)])

        

    def pop(self) -> None:
        n = len(self.stack)
        stack2 = []
        self.stack.pop()
        while self.stack:
            stack2.append([self.stack[-1][0],min(self.stack[-1][1],self.stack[-1][0])])
            self.stack.pop()
        
        self.stack = stack2[::-1]


        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()