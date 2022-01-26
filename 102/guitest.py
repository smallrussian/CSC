from tkinter import *
import tkinter
from PIL import Image, ImageTk

ws = Tk()
ws.title('Grid Example')
ws.config(bg='#E200E6')
image1=Image.open('picard.jpg')
test=ImageTk.PhotoImage(image1)
label1 = Label(ws, text='Email:', bg='#E200E6')
label2 = Label(ws, text='Password:', bg='#E200E6')

Label(ws, image=test).grid(column=0, rowspan=3)
Checkbutton(ws).grid(row=0, column=1)
Checkbutton(ws).grid(row=1, column=1)
Checkbutton(ws).grid(row=2, column=1)
label1.grid(row=0, column=2, sticky=NS)
label2.grid(row=1, column=2, sticky=E)


emailBox = Entry(ws)
pwBox = Entry(ws)

emailBox.grid(row=0, column=3)
pwBox.grid(row=1, column=3)
Label(ws, text='something', bg='red').grid(row=2, column=2, columnspan=3, ipadx=100)
loginBtn = Button(ws, text='Login', command=None)
loginBtn.grid(row=4, columnspan=2, ipady=50)
Button(ws, text='useless!', command=None).grid(row=4, column=3,ipadx=100)

ws.mainloop()