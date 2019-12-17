import time
from tkinter import *
from tkinter import messagebox
import random


root = Tk()
root.title("Save the queen")
root.geometry("950x600")

list=[0,1,2,3,4]
r1=0
r2=0
c1=0
c2=0

topframe=Frame(root)
topframe.pack()


for i in range(5):
    for j in range(5):
         label=Label(topframe,height=5,width=10,relief='solid').grid(row=i,column=j)



def action():
    global r1,r2,c1,c2
    if(r1>r2):
        for i in range(r1,r2-1,-1):
            r = i
            Label(topframe, text='R', font='Times 10', relief='solid', height=5, width=10).grid(row=i, column=c1)
            topframe.update()
            Label(topframe,relief='solid', height=5, width=10).grid(row=i, column=c1)
            # if (i == r2 ):
            #     Label(topframe, text='RQ', font='Times 10', relief='solid', height=5, width=10).grid(row=i, column=c1)
            #     messagebox.showinfo("Save the queen", "Hurrah!The queen is saved")
            #     Label(topframe, font='Times 10', relief='solid', height=5, width=10).grid(row=i, column=c1)
            time.sleep(0.5)
        if (abs(c1 - c2) == 0):
            Label(topframe, text='RQ', font='Times 10', relief='solid', height=5, width=10).grid(row=i, column=c1)
            topframe.update()
            messagebox.showinfo("Save the queen", "Hurrah!The queen is saved")


    if (r1 < r2):
        for i in range(r1,r2+1 ):
            r = i
            Label(topframe, text='R', font='Times 10', relief='solid', height=5, width=10).grid(row=i, column=c1)
            topframe.update()
            Label(topframe, relief='solid', height=5, width=10).grid(row=i, column=c1)
            time.sleep(0.5)
        if (abs(c1 - c2) == 0):
            Label(topframe, text='RQ', font='Times 10', relief='solid', height=5, width=10).grid(row=i, column=c1)
            topframe.update()
            messagebox.showinfo("Save the queen", "Hurrah!The queen is saved")



    if (c1> c2):
        if abs(r1-r2)==0:
            r=r1
        for i in range(c1,c2-1 ,-1):
            Label(topframe, text='R', font='Times 10', relief='solid', height=5, width=10).grid(row=r, column=i)
            topframe.update()
            Label(topframe, relief='solid', height=5, width=10).grid(row=r, column=i)
            if (i == c2 ):
                Label(topframe, text='RQ', font='Times 10', relief='solid', height=5, width=10).grid(row=r, column=i)
                messagebox.showinfo("Save the queen", "Hurrah!The queen is saved")
                Label(topframe, font='Times 10', relief='solid', height=5, width=10).grid(row=r, column=i)
            time.sleep(0.5)


    if(c1<c2):
        if abs(r1-r2)==0:
            r=r1
        for i in range(c1,c2+1):
            Label(topframe, text='R', font='Times 10', relief='solid', height=5, width=10).grid(row=r, column=i)
            topframe.update()
            Label(topframe, relief='solid', height=5, width=10).grid(row=r, column=i)
            if (i == c2 ):
                Label(topframe, text='RQ', font='Times 10', relief='solid', height=5, width=10).grid(row=r, column=i)
                messagebox.showinfo("Save the queen", "Hurrah!The queen is saved")
                Label(topframe, font='Times 10', relief='solid', height=5, width=10).grid(row=r, column=i)
            time.sleep(0.5)




def position():
    global r1
    r1=(random.choice(list))
    global c1
    c1=(random.choice(list))
    global r2
    r2=(random.choice(list))
    global c2
    c2=(random.choice(list))
    if(c1==c2 and r1==r2):
        c2=random.randint(0,4)


def reset_it():
    global r1
    global c1
    global r2
    global c2
    Label(topframe, height=5, width=10, relief='solid').grid(row=r1, column=c1)
    Label(topframe, height=5, width=10, relief='solid').grid(row=r2, column=c2)
    topframe.update()
    position()
    Label(topframe,text='R', height=5, width=10, relief='solid').grid(row=r1, column=c1)
    Label(topframe,text='Q',font='Times 10',height=5,width=10,relief='solid').grid(row=r2,column=c2)


reset_it()
def click_me():
    action()


bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)
start=Button(bottomframe,text="Start",fg="red",height="4",width="8",command=click_me)
reset=Button(bottomframe,text="Reset",fg="blue",height="4",width="8",command=reset_it)

start.pack(side=LEFT)
reset.pack(side=LEFT)


root.mainloop()



