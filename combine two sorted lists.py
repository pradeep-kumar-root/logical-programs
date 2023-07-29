def fn(arr1,arr2):
    res = list()
    i=j=0
    while i<len(arr1) and  j<len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i+=1
        else:
            res.append(arr2[j])
            j+=1
    res += arr1[i:] + arr2[j:]
    print(res)


arr1 = [1, 5, 6, 9, 11] 
arr2 = [3, 4, 7, 8, 10]
fn(arr1,arr2)
