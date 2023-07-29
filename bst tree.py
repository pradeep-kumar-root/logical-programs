class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val > key:
            root.left = insert(root.left,key)
        else:
            root.right = insert(root.right,key)
    return root

def inorder(root):
    if root is None:
        return
    else:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def preorder(root):
    if root is None:
        return
    else:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def printOrder(root):
    ht = height(root)
    for i in  range(1,ht+1):
        printLevel(root,i)

def printLevel(root,level):
    if root is None:
        return
    if level == 1:
            print(root.val,end=' ')
    elif level > 1:
        printLevel(root.left,level-1)
        printLevel(root.right,level-1)

def height(root):
    if root is None:
        return 0
    else:
        lh = height(root.left)
        rh = height(root.right)
        
        if lh > rh:
            return lh+1
        else:
            return rh+1

if __name__ == "__main__":
    r = Node(50) 
    r = insert(r, 30) 
    r = insert(r, 20) 
    r = insert(r, 40) 
    r = insert(r, 70) 
    r = insert(r, 60) 
    r = insert(r, 80) 
    inorder(r)
    print("------")
    preorder(r)
    print()
    printOrder(r)


