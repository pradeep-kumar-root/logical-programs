import math
def maxp(n):
    mp = -1
    while (n%2 == 0):
        mp = 2
        n /= 2
    
    for i in range(3,int(math.sqrt(n))+1,2):
        while (n%i == 0):
            mp = i
            n /= i
    
    if n>2:
        mp = n
            
    return mp

n= 100
n= 25698751364526

v=maxp(n)
print(v)
