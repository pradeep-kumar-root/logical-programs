sts = "abababaa"
stv = "pique"

import re
r'^[a-z]$|^([a-z]).*\1$'
pattern = r'^[a-z]$|^([a-z]).*\1$'
print(pattern)
if (re.search(pattern,sts)):
    print("Valid")
else:
    print("Not Valid")
