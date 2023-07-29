arr = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]


def fn(arr):
    newlist=[]
    
    for i in range(len(arr)):
        if arr[i] not in newlist:
            newlist.append(arr[i])
    print(newlist)
            
fn(arr)


