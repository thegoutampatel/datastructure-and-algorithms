
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

        #Then assign the new_node next which is None to head beacause we Intert at Begining
        #than we Assign the Address of the new_node in Head
        new_node.nextPtr = self.head
        self.head = new_node

    #Intertion at the End
    def IntertionAtEnd(self,new_data):
        #creating a new node with new data
        new_node = Node(new_data)

        #First we cheack that our linked list is not Empty
        #If the LL is empy than we assign as firt Node
        if self.head is None:
            new_node.nextPtr = self.head
            self.head = new_node

        #Now we traverse in LL --> find the last node with NextPtr is None
        temp = self.head
        while temp.nextPtr:
            temp = temp.nextPtr
        #Assign the new_node at Last
        temp.nextPtr = new_node

    def IntertionAfterAnyNode(self,prev_node,new_data):
        #first cheack that prev_node is Present or Not
        if prev_node is Node:
            print("Given node is not Present in LL")
            return
        
        #1.create a new node 
        #2.assign the prev_node nextPtr to the new_node.nextPtr --> prev contain the next node addresss
        #3.now we have to assign the prev_node new address which dis new node Address 
        
        new_node = Node(new_data)
        new_node.nextPtr = prev_node.nextPtr
        prev_node.nextPtr = new_node


    #Printing LL
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
# Llist.IntertionAtEnd(110)
Llist.IntertionAfterAnyNode(Llist.head.nextPtr.nextPtr,25)

Llist.PrintLinkedList()
        

