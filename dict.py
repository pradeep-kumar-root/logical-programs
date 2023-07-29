test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}

if "Mani" in test_dict:
    del test_dict['Mani']

print(test_dict)


dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

dict1.update(dict2)
print(sorted(dict1.items()))
print(sorted(dict1.values()))
print(sorted(dict1.keys()))
#print(sorted(dict1)


from collections import OrderedDict

od = OrderedDict([('akshat', '1'), ('nikhil', '2')])
od.update({"pradeep":'4'})
od.update({"pradeep":'4'})
print(od)

res = dict()
test_dict = {'gfg': [7, 6, 3],  
             'is': [2, 10, 3],  
             'best': [19, 4]} 
             
for k in test_dict:
    res[k] = sorted(test_dict[k])
print(test_dict)
print(sorted(test_dict))
print(res)
