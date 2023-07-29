arr = "ab45c7ph643"

def add_dig(arr):
    emp = "0"
    sum = 0
    for i in range(len(arr)):
        if arr[i].isdigit():
            emp+=arr[i]
        else:
            emp = int(emp)
            sum+=emp
            emp="0"        #sum=52, emp = "643"
    sum+=int(emp)
    print(sum)

add_dig(arr)
