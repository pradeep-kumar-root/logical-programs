class my_ds:
    def __init__(self):
        self.arr = []
        self.hasht = {}
    
    def insert(self,x):
        if x in self.hasht:
            return
        size = len(self.arr)
        self.hasht[x] = size
        self.arr.append(x)
    
    def delete(self,y):
        #{a:0,c:2}  [a,b,c]
        idx = self.hasht.get(y)
        if idx is None:
            return
        del self.hasht[y]
        last = len(self.arr) - 1
        self.arr[idx],self.arr[last] =  self.arr[last],self.arr[idx]
        #[a,c,b]
        del self.arr[last]
        #[a,c]
        self.hasht[last] = idx
    
    def search(self,z):
        return self.hasht.get(z)

ds = my_ds()
ds.insert(10)
ds.insert(20)
ds.insert(30)
ds.insert(40)
print(ds.search(30))
ds.delete(20)
ds.insert(50) 
print(ds.search(50)) 
