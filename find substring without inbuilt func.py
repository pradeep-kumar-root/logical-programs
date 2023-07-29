strr = "AAABABABABACDEFTHFDBABADR"
sub = "BABAD"



def check(strr,sub):
    start = 0
    end = 0
    while (start<len(strr)):
        if strr[start+end]!= sub[end]:
            start +=1
            end = 0
            continue
        end +=1
        
        if end == len(sub):
            return start
    return -1

s = check(strr,sub)
print(s)
