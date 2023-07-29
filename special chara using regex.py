sts = "ThisIsGeeksforGeeks!, 123"
import re
u=re.findall("[A-Z]",sts)
l=re.findall("[a-z]",sts)
n=re.findall("[0-9]",sts)
s=re.findall("[,.!?]",sts)

print(len(u),len(l),len(n),len(s))
