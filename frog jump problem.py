#Frog jump problem.
#Starts from X and goal is to reach Y. D is the distance it can cover in one jump

def frog_jump(X,Y,D):
    Z = Y-X
    if (X==Y):
        return 0
    elif ((Y-X)%D) == 0:
        return (Z/D)
    else:
        return ((Z//D)+1)

jumps = frog_jump(5,40,8)
print("Number of jumps needs to cross Y is:",jumps)
