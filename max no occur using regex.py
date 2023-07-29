import re
def maxe(sts):
    ele = re.findall("[0-9]+",sts)
    print(ele)
    sam = dict()
    for i in ele:
        if i not in sam:
            sam[i] = 1
        else:
            sam[i] += 1
    print(sorted(sam))

sts = "geek55of55geeks4abc3dr2" 
maxe(sts)
