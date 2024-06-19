from collections import deque
class MyStack:

    def __init__(self):
        self.container = deque()        

    def push(self, val: int) -> None:
        return self.container.append(val)
        

    def pop(self) -> int:
        return self.container.pop()
        

    def top(self) -> int:
        if self.empty():
            return
        else: 
            return self.container[-1]
        

    def empty(self) -> bool:
        return len(self.container) == 0
        

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(2)
param_2 = obj.pop()
print(param_2)
param_3 = obj.top()
print(param_3)
param_4 = obj.empty()
print(param_4)