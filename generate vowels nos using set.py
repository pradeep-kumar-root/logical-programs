strr = "123456789"
g = set("123456789")

print(sorted(g))

vowels = set("aeiou")
print(vowels)


strr = "geeksforgeeks"
str_new = str()
for s in strr:
    if s not in str_new:
        str_new += s
    else:
        pass

print(str_new)
    
