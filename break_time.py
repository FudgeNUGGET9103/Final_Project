import time
from tkinter import *
import tkinter.messagebox
import cv2
import os



root = tkinter.Tk()

root.title("Would you like to take a picture?")
root.geometry('500x300')
total_breaks = 1
break_count = 0
print("this program started on" + time.ctime())
while(break_count<total_breaks):
    time.sleep(3)
    
    PosNeg = []
    def yesClick():
        tkinter.messagebox.showinfo("!",  "Say Cheese")
    def noClick():
        tkinter.messagebox.showinfo("Alright, no problem",  "See you in 10 days!")
    Button1 = Button(root, activebackground="blue", command=lambda:[yesClick(), PosNeg.append(1)], text="Yes",  height=5, width=10)
    Button2 = Button(root, activebackground="red", command=lambda:[noClick(), PosNeg.append(0)], text="No", height=5, width=10)
    Button1.pack(side=LEFT)
    Button2.pack(side=RIGHT)   
    
    if 1 in PosNeg:
        vid = cv2.VideoCapture(0)
        ret, frame = vid.read()
        while(True):
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.imwrite('Desktop/butter.jpg',frame)
                cv2.destroyAllWindows()
                break
            vid.release()
        
    else:
        water = 0
    root.mainloop()        
    break_count = break_count + 1
    PosNeg.clear()
