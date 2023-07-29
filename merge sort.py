#Merge sort

arr = [1,7,5,3,9,65,23,4]

def msort(arr):
    if (len(arr) >1):
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        
        msort(L)
        msort(R)
        
        i = j = k = 0
        
        while (i<len(L) and j<len(R)):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while (i<len(L)):
            arr[k] = L[i]
            i+=1
            k+=1
        while (j<len(R)):
            arr[k] = R[j]
            j+=1
            k+=1


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
    
msort(arr)
printList(arr)
