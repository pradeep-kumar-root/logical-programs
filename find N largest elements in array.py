arr = [81, 52, 45, 10, 3, 2,100, 96]
N = 4
new_lt = list()

def largest(arr):
    for i in range(N):
        max = arr[0]
        for i in range(len(arr)):
            if arr[i] > max:
                max = arr[i]
        new_lt.append(max)
        arr.remove(max)
    print(new_lt)

largest(arr)
