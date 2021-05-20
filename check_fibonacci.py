import math
def psq(x):
    v = int(math.sqrt(x))
    return v*v == x
    
def fib(n):
    return psq(5*n*n + 4) or psq(5*n*n - 4)



while True:
    fibb = int(input("Enter the number to check fibonacci or not: "))
    n = fib(fibb)
    if n is True:
        print("Yes Fibonacci")
    else:
        print("Not Fibonacci")
        
