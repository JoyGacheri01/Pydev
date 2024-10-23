class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtBeginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next =self.head
            self.head = new.node
            
    def insertAtEnd(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
        current_node.next = new_node
            
    def printll(self):
        Current_node = self.head
        while Current_node:
            print(Current_node.data)
            Current_node = Current_node.next
            
llist = LinkedList()

llist.insertAtBeginning('J')
llist.insertAtEnd('o')
llist.insertAtEnd('Y')
llist.insertAtEnd('i like it')

print("Node data")
llist.printll()
        