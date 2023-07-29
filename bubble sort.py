def bub_sort(n):
    l = len(n)
    for i in range(0,l-1):
        for j in range(0,l-1-i):
            if (n[j] > n[j+1]):
                temp = n[j]
                n[j] = n[j+1]
                n[j+1] = temp
    print(n)
                

arr = [64, 34, 25, 12, 22, 11, 90]
bub_sort(arr)
