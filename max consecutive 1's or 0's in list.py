def fn(arr):
    count = 0
    ans = 0
    for i in range(len(arr)):
        if arr[i] == '0':
            count = 0
        
        else:
            count += 1
            ans = max(ans,count)
    print(ans)


arr = "11110000111010101010100001010000000111111"
arr = list(arr)
#arr = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1]
fn(arr)

