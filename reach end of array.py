#to Reach end of array problem

def to_reach_end(arr,n):
    jumps = [0 for i in range(n)]
    
    if (n==0 or arr[0] == 0):
        return float('inf')
    
    for i in range(1,n):
        jumps[i] = float('inf')
        for j in range(i):
            if (i<=j + arr[j]) and arr[j]!= float('inf'):
                jumps[i] = min(jumps[i],jumps[j]+1)
                break
    return jumps[n-1]

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n = to_reach_end(arr,len(arr))
print(n)
    
