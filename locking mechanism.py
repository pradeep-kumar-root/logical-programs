import threading
x = 0

def inc():
    global x
    x +=  1

def task(lock):
    for _ in range(50000):
        lock.acquire()
        inc()
        lock.release()

def thread():
    global x
    x = 0
    
    lock = threading.Lock()
    t1  = threading.Thread(target = task, args=(lock,))
    t2 = threading.Thread(target = task, args = (lock,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

if __name__ == "__main__":
    for i in range(5):
        thread()
        print("value of x {} in Iteration {}".format(x,i))
        
