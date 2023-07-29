class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next  = self.head
        self.head = new_node
        
    def delete(self,key):
        temp = self.head
        
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        
        while (temp is not None):
            if (temp.data == key):
                break
            prev = temp
            temp = temp.next
            
        if (temp is None):
            return
        prev.next = temp.next
        temp = None
    
    def print_List(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
    
    def removedup(self):
        temp = self.head
        while (temp.next is not None):
            nxt = temp.next
            if (temp.data == nxt.data):
                temp.next = nxt.next
                nxt =  None
            else:
                temp = temp.next
        return self.head
    
    def middle_ele(self):
        slow = fast = self.head
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        print(slow.data)
        
    
    def last_to_first(self):
        last = self.head
        sec_last  = None
        
        if (not last and last.next):
            return
        
        while (last and last.next):
            sec_last = last
            last =  last.next
        
        sec_last.next = None
        
        last.next = self.head
        self.head = last
        
        
llist = LinkedList() 
 
llist.push(20) 
llist.push(14) 
llist.push(13)
llist.push(11)
llist.push(11)
llist.push(11)
print ("Created Linked List: ")
llist.print_List() 
print()
#print("Linked List after removing", 
#             "duplicate elements:")
#llist.removedup()
#llist.print_List()
#llist.middle_ele()
#llist.print_List()
llist.last_to_first()
print("----------")
llist.print_List()
