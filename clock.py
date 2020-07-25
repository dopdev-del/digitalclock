from tkinter import *
from tkinter.ttk import *
from time import strftime


root = Tk()
root.title("My Clock")
root.resizable(False, False)

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text =  string)
    lbl.after(1000, time)

lbl = Label(root, font=('digital-7', 25, 'bold'),
      background= 'black',
      foreground= 'white')

lbl.pack(anchor= 'center')
time()
mainloop()

#ok i will check that issue later but as you see the clock its working cool
#i hope you like please share and suscribe