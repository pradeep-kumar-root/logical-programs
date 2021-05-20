import math,sys

def ordr(n):
    odr = 0
    while(n!=0):
        odr+=1
        n = n // 10
        
    return odr

def ams(x):
    print(sys._getframe().f_code.co_name)
    sum = 0
    tmp = int(x)
    o = int(ordr(x))
    while(tmp!=0):
        num = tmp % 10
        sum = sum + num**o
        tmp = tmp // 10
    return (sum == x)

while True:
    inp = int(input("Enter the number to check amstrong or not: "))
    res = ams(inp)
    if res is True:
        print("{} is Amstrong".format(inp))
    else:
        print("{} not Amstrong number".format(inp))
