ini_string = "123abcjw:, .@! eiw"

import re
subb = re.sub("[\W]+",'',ini_string)
print(subb)

v_str = "ankitrai326"
r_str = ""
pattern = r'[\w]$'
if re.search(pattern,v_str):
    print("Accept")
else:
    print("Discard")
    
q_str = "antique"
patt = r'^[aeiou]'

if re.search(patt,q_str):
    print("Starts with vowel")
else:
    print("Not with vowel")
    
