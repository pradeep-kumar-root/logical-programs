import re

def reg(pat,src):
    if  re.search(pat,src):
        print("Match found")
    else:
        print("Match not found")
        

src = 'kpradeep2k@gmail.com'
pat = re.compile("[a-zA-Z0-9]+@\w+.com")
reg(pat,src)

