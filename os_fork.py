import os
import time
def parentchild():
    n = os.fork()
    return n

# Driver code
s = parentchild()
if s > 0:
    time.sleep(10)
    print("Parent process : ", os.getpid())
else:
    print("Child proces : ", os.getpid())
