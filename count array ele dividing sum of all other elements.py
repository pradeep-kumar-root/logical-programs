def divide_all(arr):
    count = 0
    
    
    n = len(arr)
    
    for i in range(n):
        sum = 0              #step to be noted
        for j in range(n):
            if i==j:
                continue
            else:
                sum += arr[j]
                
        if (sum % arr[i] == 0):
            count+= 1
    
    print(count)

def my_method(arr):  #ALTERNATE OPTIMIZED SOLUTION
  sum = 0
  n = len(arr)
  for i in range(n):
    sum += arr[i]
  count = 0
  for i in range(n):
    temp = sum - arr[i]
    if temp%arr[i] == 0:
      count += 1
  print(count)

arr = [3, 10, 4, 6, 7]
divide_all(arr)
my_method(arr)
    
