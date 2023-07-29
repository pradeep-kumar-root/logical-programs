lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
dt = dict()

for e in lst:
    if e not in dt:
        dt[e] = 1
    else:
        dt[e]+=1
print(dt)
