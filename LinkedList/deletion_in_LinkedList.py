
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


    #Deletion in LinkedLind
    def DeleteNode(self,pos):
        #base case that Linkedin is not Empty
        if self.head is None:
            return
        
        #assign the head with the temp variable
        temp = self.head

        #Loop until the pos-1 value 
        for i in range(pos-1):
            temp = temp.nextPtr
            #check that 
            if temp.nextPtr is None:
                return
            
        tempPtr = temp.nextPtr.nextPtr

        temp.nextPtr = None
        
        temp.nextPtr = tempPtr

        

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
#Deletion of LinkedList at any node
Llist.DeleteNode(0)

Llist.PrintLinkedList()
        

