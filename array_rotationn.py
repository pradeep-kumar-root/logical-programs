def rotate_once(arr,n):
    temp = arr[0]
    for i in range(n):
        arr[i] = arr[i+1]
    arr[n-1] = temp
    
def rotate_arr(arr,d,n):
    for i in range(d):
        rotate_once(arr,n)
    print(arr)
    
arr = [1,5,4,7,3,8,9,3,5,9,2,5]
n = 4
d = 6
rotate_arr(arr,d,n)
