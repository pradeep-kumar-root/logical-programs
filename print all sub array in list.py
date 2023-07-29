def sublists(arr):
    subs = [[]]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            sub = arr[i:j]
            subs.append(sub)
            

    print(subs)
            
arr = [1,2,6,3,74,6,3,74,7,9,43,75,0]
sublists(arr)
