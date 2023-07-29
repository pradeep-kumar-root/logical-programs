#47198 -> 47-198 -> 47-891 -> "478"-91 -> "478"-19 ->  "47819" 

#program to find the longest palindrome in a sentence



def nxt_lar(arr,n):
    
    for i in range(n-1,0,-1):
        if arr[i] > arr[i-1]:
            break
    
    if i==1 and arr[i-1] >= arr[i]:
        print("Already largest")
        return
    
    x = arr[i-1]
    pos = i
    
    for j in range(i+1,n):
        if arr[j] > x and arr[j] < arr[pos]:
            pos = j
    
    arr[i-1], arr[pos] = arr[pos], arr[i-1]
    
    x = 0
    for j in range(i):
        x = x*10 + arr[j]
    
    arr = sorted(arr[i:])
    
    for j in range(n-i):
        x = x*10 + arr[j]
    
    print(x)

num = "534976"
num = list(map(int,num))
print(num)
n = len(num)
nxt_lar(num,n)
    
