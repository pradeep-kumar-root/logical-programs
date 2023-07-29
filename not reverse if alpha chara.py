strr = "pr@deep"
#pr@de!p -> pr@de!p -> 

def revv(strr):
    newstr = list()
    n = len(strr)
    s = 0
    newstr = [0]*(n)
    #print(newstr)
    while (s<n):
        
        if strr[n-1].isalpha() == strr[s].isalpha():
            newstr[s] = strr[n-1]
            newstr[n-1] = strr[s]
        else:
            newstr[s] = strr[s]
            newstr[n-1] = strr[n-1]
            
        s+=1
        n-=1
    print(newstr)

revv(strr)
