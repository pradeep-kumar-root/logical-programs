def Diamond(n): 
    print("Pattern 1")
    for i in range(1,(n+1)//2 +1):
        for i1 in range((n+1)//2 - i):
            print(" ",end = "")
        for i2 in range((i*2)-1):
            print("*",end = "")
        print()
    
    for j in range((n+1)//2 +1, n+1):
        for j1 in range(j - (n+1)//2):
            print(" ",end = "")
        for j2 in range((n+1 - j)*2 - 1):
            print("*",end = "")
        print()
            
            
  
# Driver Code 
# number of rows input 
rows = 23
Diamond(rows)
