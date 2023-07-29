#name, strength, health
#hit(strength,hit points), #isalive() >= 0 -> character will be alive

class Play:
    def __init__(self,name):
        self.name = name
        self.health  =  100
        
    def curr_health(self):
        return self.health
    
    def isalive(self):
        if self.health > 0:
            print("{} is alive".format(self.name))
        else:
            print("{} is dead".format(self.name))
    
    def hit(self,to,hit_points):
        if self.health!=0:
            to.health = to.health - hit_points
        

A = Play("pradeep")
B = Play("kumar")
print(B.curr_health())
A.hit(B,40)
print(B.curr_health())
print(A.curr_health())
#print(B.curr_health())
#A.isalive()
        
