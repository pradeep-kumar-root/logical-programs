class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    
    def printt_rev(self):
        temp = self.head
        while (temp.next):
            temp = temp.next
        while (temp):
            print(temp.data)
            temp = temp.prev
    
    def  printt(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
    
    def rev_ll(self):
        temp = None
        curr = self.head
        
        while (curr is not None):
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev 
        if self.head is not None:
            self.head  = temp.prev
            
            
    
if __name__ == "__main__":
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    #llist.printt_rev()
    llist.printt()
    print("------")
    llist.rev_ll()
    llist.printt()
    
