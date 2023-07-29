class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def printt(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
    
    def detect_circular(self):
        temp = self.head
        
        if temp is not None:
            while (temp):
                if (temp.next == self.head):
                    return 1
                temp = temp.next
            return 0

if __name__=='__main__': 
    llist = LinkedList()  
    llist.head = Node(1) 
    second = Node(2) 
    third = Node(3)  
    fourth = Node(4) 
      
    llist.head.next = second; 
    second.next = third; 
    third.next = fourth 
    llist.printt()
    fourth.next = llist.head
    if llist.detect_circular():
        print("Circular LL")
    else:
        print("Ordinary LL")
    
