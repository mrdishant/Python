from tkinter import *
import threading
import time
import datetime

class MyThread(threading.Thread):

    def run(self):
        i=1
        while True:
            label['text']=i
            i=i+1
            time.sleep(1)


class MyClockThread(threading.Thread):
    
    def run(self):
        
        while True:
            millis = int(round(time.time() * 1000))

            curr_time = datetime.datetime.now()
            formatted_time = curr_time.strftime('%H:%M:%S')

            clock['text']=formatted_time
            
            time.sleep(1)


def startTimer():
    myRef=MyThread()
    myRef.start()

window=Tk()

window.geometry("200x200")

clock=Label(window, text="Clock")
clock.pack()

clockT=MyClockThread()
clockT.start()

label=Label(window, text="")
label.pack()
label.place(relx=0.5, rely=0.5, anchor=CENTER)

button=Button(window,text="Start",command=startTimer)
button.pack()
button.place(relx=0.5, rely=0.6, anchor=CENTER)

window.mainloop()