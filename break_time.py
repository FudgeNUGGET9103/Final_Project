import time
from datetime import date
from tkinter import *
import tkinter.messagebox

break_count = 0
root = tkinter.Tk()
root.title("Would you like to take a picture?")
root.geometry('500x300')        
print("this program started on" + time.ctime())
PosNeg = []
def yesClick():
    tkinter.messagebox.showinfo("!",  "Say Cheese")

def noClick():
    tkinter.messagebox.showinfo("Alright, no problem",  "See you in 10 days!")

Button1 = Button(root, activebackground="blue", command=lambda:[yesClick(), PosNeg.append(1)], text="Yes",  height=5, width=10)
Button2 = Button(root, activebackground="red", command=lambda:[noClick(), PosNeg.append(0)], text="No", height=5, width=10)
Button1.pack(side=LEFT)
Button2.pack(side=RIGHT)
root.mainloop()
break_count = break_count + 1
time.sleep(5)
if 1 in PosNeg:
    time.sleep(1)
    import cv2
    vid = cv2.VideoCapture(0)
    ret, frame = vid.read()
    while(True):
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite('Desktop/{}.jpg'.format(date.today()),frame)
            cv2.destroyAllWindows()
            break
    vid.release()
    del cv2
