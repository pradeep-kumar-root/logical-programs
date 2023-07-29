class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_start(self,node):
        new_node = Node(node)
        
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_value(self,prev_data,node):
        if prev_data is None:
            self.head  = node
            return
        new_node = Node(node)
        new_node.next = prev_data.next
        prev_data.next = new_node
    
    def insert_at_end(self,node):
        new_node = Node(node)
        if self.head is None:
            self.head  = new_node
            return
        
        temp = self.head
        while (temp.next):
            temp = temp.next
        temp.next = new_node
    
    def printt(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
    
    def delete_key(self,key):
        temp = self.head
        
        if temp is not None:
            if temp.data == key:
                temp.next = self.head
                temp = None
                return
        
        while (temp is not None):
            if temp.data == key:
                break
            prev =  temp
            temp = temp.next
            
        if (temp == None):
            return
        
        prev.next = temp.next
        temp = None
    
    def delete_pos(self,pos):
        temp = self.head
        
        if pos == 0:
            temp.next = self.head
            temp = None
            
        for i in range(0,pos-1):
            temp = temp.next
        
        if (temp or temp.next) is None:
            return
        
        prev  = temp
        temp = temp.next
        
        prev.next =  temp.next
        temp = None
    
    def detect_loop_remove(self):
        slow = fast = self.head
        while (slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                self.removeLoop(slow)
                return 1
        return 0
    
    def removeLoop(self,loop_node):
        p1  = self.head
        while(1):
            
            p2 = loop_node
        
            while (p2.next!= loop_node and p2.next!= p1):
                p2 = p2.next
        
            if p2.next ==  p1:
                break
            
            p1 =  p1.next
        p2.next = None
    
    def  rev_ll(self):
        curr = self.head
        prev = None
        while (curr is not None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
        
            
            
        
if __name__=='__main__': 
  
    
    llist = LinkedList() 
  
    
    llist.insert_at_end(6) 
  
     
    llist.insert_at_start(7); 
  
    
    llist.insert_at_start(1); 
  
    
    llist.insert_at_end(4) 
  
     
    llist.insert_at_value(llist.head.next, 9) 
  
    print('Created linked list is:') 
    #llist.printt()
    
    #llist.delete_key(9)
    
    #llist.printt()
    
    #llist.delete_pos(2)
    
    
    
    llist.head.next.next.next.next.next = llist.head.next.next
    
    
    
    llist.detect_loop_remove()
    
    #llist.printt()
    
    #llist.printt()
    
    llist.rev_ll()
    
    llist.printt()
    
