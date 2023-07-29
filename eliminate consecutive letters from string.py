def eliminate(s):
    j = 0
    for i in range(len(s)):
        if (s[i]!= s[j]):
            j+=1
            s[j]=s[i]
    j+=1
    s=s[:j]
    return s

s = "aaabbbccca"
s = list(s)
s = eliminate(s)
print(s)
