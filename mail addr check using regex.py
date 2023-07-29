stq = "ankitrai326@gmail.com"
patt = r'^[a-zA-Z][a-zA-Z0-9_!]+@[a-z]{3,15}.com'

import re
if re.search(patt,stq):
    print("Valid mail address")
else:
    print("Not valid mail address")
