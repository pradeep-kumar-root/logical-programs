strr = "GeeksforGeeks"
subs = "for"
v = str()
def check(strr,subs):
    if (strr.find(subs) == -1):
        print("substring not found")
    else:
        print("substring found")

check(strr,subs)
