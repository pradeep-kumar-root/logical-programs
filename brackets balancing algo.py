
def balanced(sts):
    stack = []
    for c in sts:
        if c in ["(","{","["]:
            stack.append(c)
        else:
            if not stack:
                return False
            currrent_c = stack.pop()
            if currrent_c == "(":
                if c!= ")":
                    return False
            if currrent_c == "{":
                if c!= "}":
                    return False
            if currrent_c == "[":
                if c!= "]":
                    return False
    if stack:
        return False
    return True

sts = "{([](){}{})}"

if balanced(sts):
    print("Balanced")
else:
    print("Unbalanced")
            
                
            
            

            
            


