from collections import defaultdict

class Node:
    def __init__(self):
        self.children = defaultdict()
        self.terminating = False

class Trie:
    def __init__(self):
        self.root = self.get_node()
    
    def get_node(self):
        return Node()
    
    def index(self,ch):
        return ord(ch) - ord('a')
    
    def insert(self,key):
        root = self.root
        length  = len(key)
        
        for i in range(length):
            idx =  self.index(key[i])
            
            if not idx in root.children:
                root.children[idx] = self.get_node()
            root = root.children.get(idx)
        
        root.terminating = True
    
    def search(self,key):
        root = self.root
        length = len(key)
        
        for i in range(length):
            idx =  self.index(key[i])
            
            if root is None:
                return False
            root = root.children.get(idx)
        
        return True if root and root.terminating else False
    
    def delete(self,key):
        root = self.root
        length = len(key)
        
        for i in range(length):
            idx =  self.index(key[i])
            if not root:
                print("Word not found")
                return -1
            root = root.children.get(idx)
        
        if not root:
            print("Word not found")
            return -1
        else:
            root.terminating = False
            return 0
    
    def update(self,new,old):
        val = self.delete(old)
        if val == 0:
            self.insert(new)

if __name__ == "__main__":

    strings = ["pqrs", "pprt", "psst", "qqrs", "pqrs"]

    t = Trie()
    for word in strings:
        t.insert(word)

    print(t.search("pqrs"))
    print(t.search("pprt"))

    t.delete("pprt")

    print(t.search("pprt"))

    t.update("mnop", "pprt")
        
