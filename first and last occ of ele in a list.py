def fn(arr,x):
    first = last = -1
    for i in range(len(arr)):
        if arr[i]!= x:
            continue
        else:
            if (first==-1):
                first = i
            last =  i
    if first!=-1:
        print("First occurence is {} and last occurence is {}".format(first,last))
    else:
        print("Element not found")

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8 ]
fn(arr,8)
