class myclass:
    sts = "cde"
    def __init__(self,name):
        self.name = name
        

myc = myclass("Pradeep")
cym = myclass("kumar")
print(myc.name)
print(cym.name)
cym.name = "Pradeep"
print(cym.name)



print(myc.sts)
myc.sts = "vde"
print(myc.sts)
print(myclass.sts)
