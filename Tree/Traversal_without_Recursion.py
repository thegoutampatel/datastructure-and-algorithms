#Create a Node which containes data left pointer and right pointer data
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

#Implementation of PreOrder Traversal without using the Recursion
def preOrder(root):
    if root is None:
        return
    
    stack = []
    stack.append(root)

    while len(stack) > 0:
        Popped = stack.pop()
        print(str(Popped.data) + " " , end=' ')
        if Popped.right:
            stack.append(Popped.right)

        if Popped.left:
            stack.append(Popped.left)

def inOrder(root):
    stack = []
    current = root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif len(stack) > 0:
            current = stack.pop()
            print(str(current.data) + " " , end=" ")
            current = current.right
        else:
            break
        
         
def postOrder(root):
    stack1 = []
    stack2 = []
    stack1.append(root)
    while len(stack1) > 0:
        current = stack1.pop()
        stack2.append(current.data)

        if current.left:
            stack1.append(current.left)
        
        if current.right:
            stack1.append(current.right)

    while stack2:
        data = stack2.pop()
        print(str(data) + " ", end=' ')


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)
print("PreOrder : ")
preOrder(root) 
print(" ")
print("InOrder")
inOrder(root) 
print(" ")
print("PostOrder")
postOrder(root)  