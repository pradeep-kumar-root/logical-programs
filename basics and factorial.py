print(1, 2, 3, 4, sep='#', end='&')

sam_list = [1,2,3,4,5,6,7,8,9]
sec_list = [9,8,7,6,5,4,3,2,1]

print(sam_list[3:8])

d = {1:'value','key':2}
print(d[1])
print(d['key'])
print(d)
print(d.items())
print(d.keys())
print(d.values())


print("this is the format block {} and second is this {} ".format(type(1),type("str")))
s = dict([[1,2],[5,7]])
print(s)

#nos = int(input("Enter the number of values to be entered: "))
#sample_dt = dict(input().split(" ") for i in range(nos))
#print(sample_dt)

def simple_df():
    print("in function assignment")

s = simple_df
s()


#for val in "sequence":
#    if val == 'q':
#        continue
#    print(val)


def simp(*names):
    for n in names:
        print(n)

simp("Pradeep","Kumar","Bama")

def fac(n):
    return 1 if (n==1 or n==0) else n*fac(n-1)

s = int(input("Enter the number to calc Factorial: "))
res = fac(s)
print("Factorial of {} is {}".format(s,res))
