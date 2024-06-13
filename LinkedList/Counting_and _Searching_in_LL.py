class Node:
    def __init__(self,data):
        self.data = data
        self.nextPtr = None

class LinkedList:
    def __init__(self):
        self.head = None

    #Intertion at the Begining 
    def IntertionAtBeginning(self,new_data):
        #First Creating a new node with new data
        new_node = Node(new_data)
        new_node.nextPtr = self.head
        self.head = new_node

    #Counting of Nodes in LL
    def CountingLL(self):
        temp = self.head
        count = 0
        while temp:
            temp = temp.nextPtr
            count+=1
            
        return print(count)
    
    #Searching the Node in LL
    def SearchNode(self,Nodedata):
        temp = self.head
        
        while temp:
            if temp.data == Nodedata:
                return True
            else:
                temp = temp.nextPtr
        return False
        

    def PrintLinkedList(self):
        temp = self.head

        while temp:
            print(str(temp.data) + " ", end=" ")
            temp = temp.nextPtr

Llist = LinkedList()
Llist.IntertionAtBeginning(10)
Llist.IntertionAtBeginning(20)
Llist.IntertionAtBeginning(30)
Llist.IntertionAtBeginning(40)
Llist.IntertionAtBeginning(50)
Llist.PrintLinkedList()
print()

#Couting the Nodes
# Llist.CountingLL()

#Searching the Node
result = Llist.SearchNode(10)

if result == True:
    print("Given Node is Present in LinkedList")
else:
    print("Given Node is Not Present in LinkedList")