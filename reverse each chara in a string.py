sts = "This is a sample program"

def rev_words(sts):
    lt = list()
    lt = sts.split(" ")
    print(lt)
    
    n = [i[::-1] for i in lt]
    res = " ".join(n)
    print(res)
        

rev_words(sts)
