#binary search

arr = [10, 22, 28, 29, 30, 40] 
x = 54

def nxtgre(arr,x):
    n=len(arr)
    diff = float('inf')
    for i in range(n):
        for j in range(i+1,n):
            y = abs(arr[i]+arr[j] - x)
            if y < diff:
                diff = y
                l = arr[i]
                r = arr[j]
    return l,r

r1,r2 = nxtgre(arr,x)
print(r1,r2)
    
                

