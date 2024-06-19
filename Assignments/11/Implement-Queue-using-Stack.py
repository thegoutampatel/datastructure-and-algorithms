from collections import deque
class MyQueue:

    def __init__(self):
        self.container = deque()

    def push(self, X: int) -> None:
        return self.container.appendleft(X)

    def pop(self) -> int:
        return self.container.pop()
        
    def peek(self) -> int:
        if self.empty():
            return
        else:
            return self.container[-1]
        

    def empty(self) -> bool:
        return len(self.container) == 0
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(2)
param_2 = obj.pop()
print(param_2)
param_4 = obj.empty()
print(param_4)