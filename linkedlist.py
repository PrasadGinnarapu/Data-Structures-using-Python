
class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

 
class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_LL(self):
        '''Traversing all Nodes'''
        if self.head is None:
            print("Linked List is Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.ref
                
    def add_begin(self,data):
        '''Add a Node at Begining'''
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
        
    def add_ending(self,data):
        '''Add a Node at End Position'''
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n=n.ref
            n.ref = new_node
            
    def add_afterNode(self,data,x):
        '''Add a Node after a given Node'''
        n = self.head
        while n is not None:
            if x==n.data:
                break
            n = n.ref
        
        if n is None:
            print("Node is not present")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
             
            
            
ll = LinkedList()
ll.add_ending(100)
ll.add_begin(50)
ll.add_ending(200)
ll.add_begin(20)
ll.add_afterNode(30,20)
ll.print_LL()