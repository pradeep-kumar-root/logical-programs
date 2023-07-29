sts = "GeeksforGeeks"
char_freq = dict()

for s in sts.casefold():
    if s not in char_freq:
        char_freq[s] = 1
    else:
        char_freq[s] += 1
        
res = min(char_freq,key = char_freq.get)
