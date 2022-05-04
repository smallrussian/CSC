from tkinter import *
from tkinter.scrolledtext import ScrolledText
import final_project2 as fp2
window = Tk()

#scrollbar

#ScrolledText(window).pack()
phone_number=""
###saves the phone number into memory
def save_number(number):
    return number

#image
canvas = Canvas(window, width = 608, height = 420)
canvas.pack()
img = PhotoImage(file = "alarmapplogo420h.png")
canvas.create_image(20,20, anchor = NW, image=img)
#create button
###i made the button activate the motion detection program, which i have integrated 
btn = Button(window, text = "submit", fg = '#102A3D', bg = "#BCBEC0", command=lambda: fp2.detectMotion(save_number(txtfld.get())))
btn.place(x= 400, y=570)

#top label
label = Label(window, text = "Add phone number to get notified of movement", bg = '#102A3D', fg = "#BCBEC0")
label.place(x= 50, y= 300)

#label 1
lblfld = Label(window, text = "Phone number:", fg = "#BCBEC0", bg = '#102A3D' )
lblfld.place(x = 50, y= 340)

#entry box 
txtfld = Entry(window, text = "Phone num", bd = 5)
txtfld.place(x= 180, y= 335)


###main program###
window.title("security system")
window.geometry("393x420")
window.mainloop()

