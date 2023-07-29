test_dict = {'gfg' : [5, 6, 7, 8], 
             'is' : [10, 11, 7, 5], 
             'best' : [6, 12, 10, 8], 
             'for' : [1, 2, 5]} 
             

st = list()
for s in test_dict.values():
    st.append(s)

print(sorted(st))
vall = sorted(st)
print(vall)
vals = list()
for i in vall:
    for j in i:
        if j not in vals:
            vals.append(j)

print(vals)
