def partition(arr,start,end):
    pivot = arr[start]
    low = start+1
    high = end
    
    while (1):
        while (low<=high and arr[high] >= pivot):
            high = high - 1
        while (low<=high and arr[low] <= pivot):
            low = low + 1
        
        if low <= high:
            arr[low],arr[high]  = arr[high],arr[low]
        else:
            break
        
    arr[start],arr[high] = arr[high],arr[start]
    
    return high
    
def quicksort(arr,start,end):
    if start >= end:
        return
    
    p = partition(arr,start,end)
    quicksort(arr,start,p-1)
    quicksort(arr,p+1,end)
    
arr = [1,6,4,7,3,6,2,0]
quicksort(arr,0,len(arr)-1)

print(arr)
