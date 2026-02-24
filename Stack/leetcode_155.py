'''
using an approach to store [val, min] for every stack object is the key
to solving this problem.
'''

class MinStack:

    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, val: int) -> None:
        if self.size == 0:
            self.stack.append([val,val])
        else:
            get_min = self.getMin()
            if val < get_min:
                self.stack.append([val,val])
            else:
                self.stack.append([val,get_min])
        self.size+=1

    def pop(self) -> None:
        if self.size == 0:
            return
        self.stack.pop(-1)
        self.size-=1

    def top(self) -> int:
        if self.size == 0:
            return 
        return self.stack[-1][0]

    def getMin(self) -> int:
        if self.size == 0:
            return
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()