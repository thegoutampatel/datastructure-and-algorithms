#Create a Node which containes data left pointer and right pointer data
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

#mplementation of Pre Order Traversal 
def preOrder(root):
    if root:
        #Printin the Root Data
        print(str(root.data) + " " , end=' ')
        #With the help of recursion Traverse Left Tree
        preOrder(root.left)
        #With the help of recursion Traverse Right Tree
        preOrder(root.right)



#Implementaion of In Order Traversal
def inOrder(root):
    if root:
        #using recursion for left tree traverse
        inOrder(root.left)
        print(str(root.data) + " " , end=' ')
        #using recursion for Right Tree Traverse   
        inOrder(root.right)


#Implementation of Post Order Traversal
def postOrder(root):
    if root:
        #Recursion for Left
        postOrder(root.left)
        #Recutsion for right
        postOrder(root.right)
        print(str(root.data) + " " , end=' ')


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