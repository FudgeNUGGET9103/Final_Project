import webbrowser
import time
from tkinter import *
import tkinter.messagebox
import webbrowser

total_breaks = 1
break_count = 0
root = tkinter.Tk()

root.title("Would you like to take a picture?")
root.geometry('500x300')

print("this program started on" + time.ctime())
while(break_count<total_breaks):
    time.sleep(5)
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
    if 1 in PosNeg:
        webbrowser.open("https://docs.google.com/document/d/1rfOX_yNOablm8fOgGUvYkLISBOm6cUMJF7Y9O5LUKJU/edit#")
    else:
        water = 0
    break_count = break_count + 1
    print(PosNeg)


