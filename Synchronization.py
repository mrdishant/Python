import threading
import time

lock=threading.Lock()

stack=[]

class Thread1(threading.Thread):

    def run(self):
        lock.acquire()
        for i in range(1,11):
            stack.append(i)
            print(stack)
        lock.release()
        


class Thread2(threading.Thread):
    
    def run(self):
        i=1
        lock.acquire()
        for i in range(0,len(stack)):
            stack.pop()
            print(stack)
        lock.release()
        


thread1=Thread1()

thread2=Thread2()

thread1.start()

thread2.start()
