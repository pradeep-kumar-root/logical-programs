#program to find the longest palindrome in a sentence

s = "My name is ava and i love Geeksforgeeks"
def chk_palin(s):
    if s == s[::-1]:
        return 1
    else:
        return 0
        
def long_palin(s):
    lt=pal= []
    lt = s.split(" ")
    for i in lt:
        if (chk_palin(i)):
            pal.append(i)
    print(pal)
    res = sorted(pal,key=len)
    print(res[-1])
   

long_palin(s)
