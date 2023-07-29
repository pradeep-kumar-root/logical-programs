vtq = "Geeks"

import re
pattern = r'^[A-Z]+[a-z]+|[a-z]+[A-Z]+'
if re.search(pattern,vtq):
    print("Valid")
else:
    print("Not Valid")
    
