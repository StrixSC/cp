"""
Runtime 54 ms Beats 97.69% 
Memory 18.4 MB Beats 26.17% -> Memory is not the best, but it is inevitable considering we need to store tuples of every element we add and their local minimum.
"""

class MinStack:
    def __init__(self):
        self.stack = []

    # Each val, when added in the stack, will hold a "local" minimum.
    # The local minimum is simply the minimum of the previous top of the stack with itself.
    # Because this is a stack, every element we add will simply check if it is smaller than the top of the stack's local minimum, which will inturn show that
    # the local minimum is actually the global minimum
    def push(self, val: int) -> None:
        if self.stack:
            lmin = self.getMin()
            if val <= lmin:
                lmin = val
        else:
            lmin = val

        self.stack.append((val, lmin))

    def pop(self) -> None:
        self.stack.pop()
        
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