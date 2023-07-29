sts = "aaabbddaabbaa"

def count_char(sts):
    count = 1
    length = ""
    if len(sts)>1:
        for i in range(1,len(sts)):
            if sts[i-1] == sts[i]:
                count += 1
            else:
                length += str(count) + sts[i-1]
                count = 1
        length += str(count) + sts[i-1]
    else:
        i = 0
        length += str(count) + sts[0]
    print(length)

count_char(sts)
