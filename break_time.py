# import everything from tkinter module
from tkinter import *
  
# import messagebox from tkinter module
import tkinter.messagebox
  
# create a tkinter root window
root = tkinter.Tk()
  
# root window title and dimension
root.title("Picture time")
root.geometry('500x300')
  
# Create a messagebox showinfo
  
def onClick():
    tkinter.messagebox.showinfo("Would you like to take a picture?",  "Hi I'm your message")
  
# Create a Button
button = Button(root, text="Yes", command=onClick, height=5, width=10)
  
# Set the position of button on the top of window.
button.pack(side='bottom')
root.mainloop()




import webbrowser
import time



total_breaks = 3
break_count = 0

print("this program started on" + time.ctime())
while(break_count<total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=9tXVK7fh-kI")
    break_count = break_count + 1
    

