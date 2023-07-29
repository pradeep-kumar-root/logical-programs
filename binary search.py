#binary search

def bin_sear(arr,l,r,x):
    if r>=1:
        mid = l + (r-l)//2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return bin_sear(arr,l,mid-1,x)
        else:
            return bin_sear(arr,mid+1,r,x)
    else:
        return -1
    
arr = [1,2,3,4,5,6,7,8,9]
x = 8
res = bin_sear(arr,0,len(arr)-1,x)
if res!= -1:
    print("Element present at index {}".format(res))
else:
    print("element not present in list")
