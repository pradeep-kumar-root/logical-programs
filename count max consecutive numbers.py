arr = [1,2,3,1,5,6]

def cons(arr):
    arr.sort() #[1,1,2,3,5,6]
    
    v = []
    n = len(arr)
    for i in range(n):
        if arr[i] not in v:
            v.append(arr[i]) #[1,2,3,5,6]
    
    ans = 0
    count  = 1
    for i  in range(1,len(v)):
        if ((v[i-1] +1) == v[i]):
            count += 1
        else:
            count = 1
        ans = max(count,ans)
    print(ans)
            


cons(arr)
