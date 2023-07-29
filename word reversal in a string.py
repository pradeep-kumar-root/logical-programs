strr = "geeks quiz practice code"

def rev(strr):
    strr1 = strr.split(" ")
    print(strr1)
    rev_str = " ".join(strr1[::-1])
    print(rev_str)
    
rev(strr)
