
from tkinter import *
from guess_indian_gender import IndianGenderPredictor
from tkinter import messagebox

root = Tk()
root.geometry('550x350')
root.resizable(0,0)
root.title("GenderDetector")

myname =''



def click_me():
    global myname
    myname=entry_name.get("1.0",'end-1c')
    i = IndianGenderPredictor()
    messagebox.showinfo("Gender",i.predict(myname))

def reset_it():
    entry_name.delete('1.0', END)

topframe = Frame(root)
topframe.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

label1 = Label(topframe, text='Name',fg='green',font='Times 22',width=20,height=2)
label1.pack()

entry_name = Text(topframe, height=5, width=20)
entry_name.pack()

save = Button(bottomframe,text='save', fg='green', font='12',command=click_me, height=1,width=4).grid(row = 0,column = 1)
reset = Button(bottomframe,text='Reset', fg='red', font='12',command=reset_it, height=1,width=4).grid(row = 0,column = 2)



root.mainloop()