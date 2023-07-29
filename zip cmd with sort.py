x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
y = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]

new_lt = list()
new_ltt = zip(y,x)
for e in sorted(new_ltt):
    new_lt.append(e)
print(new_lt)
