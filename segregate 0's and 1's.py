sts = [1,0,1,0,0,0,1,1,1,1,1,1,0,0,1,0,0,0,1,1,0]
#sts = [0,1,1,1,0]
l_sts = len(sts)
print(l_sts)
count = 0
for i in range(l_sts):
    if sts[i]==0:
        count += 1
print(count)

new_sts = list()
for i in range(0,count):
    sts[i] = 0

for j in range(count,l_sts):
    sts[j] = 1

print(sts)
    
