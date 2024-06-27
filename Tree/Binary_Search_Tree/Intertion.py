#Creating a class of a node in a Binary Search Tree
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


#Intertion of a Node in Binary Seach Tree
def insertBST(root,key):
    #tree is Emty
    if root is None:
        return Node(key)
    
    else:
        if root.data == key:
            return root
        elif root.data < key:
            root.right = insertBST(root.right, key)
        else:
            root.left  = insertBST(root.left, key)
    
    return root

def searchBST(root, searchData):
    #Base condition
    if root is None or root.data == searchData:
        return root
    
    #right Recursive code
    if root.data < searchData:
        return searchBST(root.right, searchData)

    return searchBST(root.left, searchData)

#inorder Traversal
def InOrder(root):
    if root:
        InOrder(root.left)
        print(str(root.data) + " " , end=" ")
        InOrder(root.right)


#driver Code
root = Node(50)
root = insertBST(root, 40)
root = insertBST(root, 70)
root = insertBST(root, 60)
root = insertBST(root, 80)

#after Inorder Traversal if we get sorted arry we can say that it is a Bianry Seach Tree
print("Inorder Traversal of the Tree")
InOrder(root)
print()

searchData = 100
if searchBST(root,searchData):
    print("search data is present in BST")
else:
    print("seach data is not present in BST")