for i in range(1,100):
    if i>1:
        for j in range(2,i):
            if i%2==0:
                break
        else:
            print(i)
