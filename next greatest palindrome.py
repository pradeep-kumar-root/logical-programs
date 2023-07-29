
def nxtpal(arr):
    n = len(arr)
    if (arr.count('9') == n):
        print(int(arr)+2)
    else:
        if n%2==0:
            mid = n//2
            a = int(arr[:mid])
            new_no = int(str(a) + str(a)[::-1])
            if new_no > int(arr):
                print(new_no)
            else:
                new_no = int(str(a+1) +  str((a+1))[::-1])
                print(new_no)
        
        else:
            mid = n//2 +1
            a = int(arr[:mid])
            new_no = int(str(a) + str((a))[:mid-1][::-1])
            if new_no > int(arr):
                print(new_no)
            else:
                new_no = int(str(a+1) + str((a+1))[:mid-1][::-1])
                print(new_no)

arr = "54163"
nxtpal(arr)
