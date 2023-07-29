def fn_min(arr):
  counter = 0
  min = float("inf")

  n = len(arr)
  #print(n)
  for i in range(n-1,-1,-1):
      #print(i)
      if (arr[i] > min):
          counter += 1
      elif (arr[i] <= min):
          min = arr[i]
  
  print(counter)

arr = [2,1,2,3,4,5] 
fn_min(arr)
