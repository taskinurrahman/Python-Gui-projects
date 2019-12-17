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
r3=0
r4=0
c1=0
c2=0
c4=0
c3=0



topframe=Frame(root)
topframe.pack()


for i in range(5):
    for j in range(5):
         label=Label(topframe,height=5,width=10,relief='solid').grid(row=i,column=j)



def action():
    global r1,r2,c1,c2

    for i in range(5):
        if(i%2==0):
            for j in range(5):
                label = Label(topframe,text='V', height=5, width=10, relief='solid').grid(row=i, column=j)
                topframe.update()
                label = Label(topframe, height=5, width=10, relief='solid').grid(row=i, column=j)

                time.sleep(1)

        else:
            for j in range(4,-1,-1):
                label = Label(topframe,text='V' ,height=5, width=10, relief='solid').grid(row=i, column=j)
                topframe.update()
                label = Label(topframe, height=5, width=10, relief='solid').grid(row=i, column=j)
                if(i==4 and j==4):
                   messagebox.showinfo("cleaner","All tiles cleaned")
                time.sleep(1)




def position():
    global r1
    r1=(random.choice(list))
    global c1
    c1=(random.choice(list))
    global r2
    r2=(random.choice(list))
    global c2
    c2=(random.choice(list))
    global  r3
    r3 = (random.choice(list))
    global  c3
    c3 = (random.choice(list))
    global  r4
    r4 = (random.choice(list))
    global c4
    c4 = (random.choice(list))



def reset_it():
    global r1
    global c1
    global r2
    global c2
    Label(topframe, height=5, width=10, relief='solid').grid(row=0, column=0)
    Label(topframe, height=5, width=10, relief='solid').grid(row=r1, column=c1)
    Label(topframe, height=5, width=10, relief='solid').grid(row=r2, column=c2)
    Label(topframe, height=5, width=10, relief='solid').grid(row=r3, column=c3)
    Label(topframe, height=5, width=10, relief='solid').grid(row=r4, column=c4)
    topframe.update()
    position()
    Label(topframe,text='D', height=5,width=10,relief='solid').grid(row=r1, column=c1)
    Label(topframe,text='D',height=5,width=10,relief='solid').grid(row=r2,column=c2)
    Label(topframe, text='D', height=5, width=10, relief='solid').grid(row=r3, column=c3)
    Label(topframe, text='D', height=5, width=10, relief='solid').grid(row=r4, column=c4)
    Label(topframe, text='V', height=5, width=10, relief='solid').grid(row=0, column=0)


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



