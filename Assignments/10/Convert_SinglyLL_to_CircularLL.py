
class Node:
    def __init__(self,data):
        self.data = data
        self.nextPtr = None

class LinkedList:
    def __init__(self):
        self.head = None

    def IntertionAtBeginning(self,new_data):
        #First Creating a new node with new data
        new_node = Node(new_data)
        new_node.nextPtr = self.head
        self.head = new_node

    def SinglyToCircular(self):
        temp = self.head

        while temp.nextPtr:
            temp = temp.nextPtr
        
        temp.nextPtr = self.head


      ## to detect the loop inside the linked list
    def detectLoop(self):
        hare = self.head
        tortoise = self.head

        while tortoise and hare and hare.nextPtr:
            hare = hare.nextPtr.nextPtr
            tortoise = tortoise.nextPtr

        if tortoise == hare:
            return True
        return False

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


Llist.SinglyToCircular()
Llist.PrintLinkedList()

if Llist.detectLoop():
  print("Loop is inside the Linked List")
else:
  print("No Loop")
        

