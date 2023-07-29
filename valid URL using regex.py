strr = "https://www.geeksforgeeks.org/"

import re
pattern = r'(http|https)://(www.)[a-zA-Z0-9!@#$%^&*]+.(com|org|gov|in)'
fp = re.search(pattern,strr)
if re.search(pattern,strr):
    print("Valid URL")
else:
    print("Not valid URL")
print(fp.group(1,2,3))
    


pars = "https://www.geeksforgeeks.org/courses"
patte = r'(http|https)://(www.)([a-zA-Z0-9!@#$%^&*]+.)(com|org|gov|in)'

res = re.search(patte,pars)
   
lt = res.group(3,4)
ltt = ''.join(lt)
print(ltt)
