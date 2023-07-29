#Producer consumer problem
from threading import Thread,Semaphore
import time,random
queue = []
max_len = 15
sem = Semaphore()

class Producer(Thread):
    def run(self):
        global queue
        while True:
            sem.acquire()
            if len(queue) == max_len:
                print("Queue is full")
                sem.release()
                
            
            r = random.randint(0,9)
            queue.append(r)
            print("Produced is",r)
            sem.release()
            time.sleep(random.random())

class Consumer(Thread):
    def run(self):
        global queue
        while True:
            sem.acquire()
            if len(queue) == 0:
                print("Queue is empty")
                sem.release()
            
            r = queue.pop(0)
            print("Consumed is",r)
            sem.release()
            time.sleep(random.random())

def thread():
    Producer().start()
    Consumer().start()

if __name__ == "__main__":
    thread()
        
