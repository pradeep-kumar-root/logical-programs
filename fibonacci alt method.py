def fibonacci(nos):
    if (nos<=0):
        print("Enter valid numbers")
    elif (nos==1):
        print("Fibonacci series is: 0")
    else:
        n1,n2 = 0,1
        c = 0
        while c < nos:
            print(n1)
            nnet = n1+n2
            n1 = n2
            n2 = nnet
            c+=1
nos = int(input("Enter number of Fibonacci elements to display:"))
fibonacci(nos)
