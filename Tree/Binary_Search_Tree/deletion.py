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

def minNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

#Deletion in BST
def deletionBST(root, deleteData):
    if root is None:
        return root
    elif root.data > deleteData:
        root.left = deletionBST(root.left, deleteData)
    elif root.data < deleteData:
        root.right = deletionBST(root.right, deleteData)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        else:
            tempnode = minNode(root.right)
            root.data = tempnode.data
            root.right = deletionBST(root.right, tempnode.data)
    return root


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

deleteData = 80
deletionBST(root, deleteData)
InOrder(root)