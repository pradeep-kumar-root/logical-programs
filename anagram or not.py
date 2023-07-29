def anagram(s1,s2):
    dict1 = dict()
    dict2 = dict()
    if len(s1)!= len(s2):
        print("Strings are not in anagram")
        return 
    else:
        for s in s1:
            if s not in dict1:
                dict1[s] = 1
            else:
                dict1[s] += 1
        
        for r in s2:
            if r not in dict2:
                dict2[r] = 1
            else:
                dict2[r] += 1
    
    if dict1 == dict2:
        print("anagram")
    else:
        print("Strings are not in anagram")


s1 = "test"
s2 = "tset"
anagram(s1,s2)
