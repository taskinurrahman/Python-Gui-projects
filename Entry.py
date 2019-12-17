from tkinter import *


root = Tk()
root.geometry('550x350')
root.resizable(0,0)
root.title("Entry")

list=[]


zilla=["Barguna","Barisal","Bhola","Jhalokati","Patuakhali", "Pirojpur",
"Bandarban","Brahmanbaria", "Chandpur", "Chittagong", "Comilla","Cox's Bazar","Feni",
"Khagrachhari","Lakshmipur","Noakhali", "Rangamati","Dhaka","Faridpur","Gazipur","Gopalganj",
"Kishoreganj","Madaripur", "Manikganj","Munshiganj","Narayanganj","Narsingdi","Rajbari","Shariatpur","Tangail",
"Bagerhat", "Chuadanga", "Jessore",  "Jhenaidah","Khulna","Kushtia","Magura","Meherpur","Narail","Satkhira",
"Jamalpur", "Mymensingh","Netrakona","Sherpur","Bogra","Chapainawabganj","Joypurhat","Naogaon","Natore","Pabna",
"Rajshahi", "Sirajganj","Dinajpur", "Gaibandha", "Kurigram", "Lalmonirhat","Nilphamari", "Panchagarh", "Rangpur",
"Thakurgaon","Habiganj","Moulvibazar","Sunamganj","Sylhet"]

departments=['EEE','CSE','CE','ME']


name=''
email=''
mobile=''
district=''
dept=''

def click_me():
    input()
    action()
    output()



def input():
    list.append(entry_name.get())
    list.append(entry_email.get())
    list.append(entry_mobile.get())
    list.append( entry_dist.get())
    list.append( entry_dept.get())

def output():
    entry_name.delete(0,END)
    entry_name.insert(0,name)
    entry_email.delete(0,END)
    entry_email.insert(0,email)
    entry_mobile.delete(0,END)
    entry_mobile.insert(0,mobile)
    entry_dist.delete(0,END)
    entry_dist.insert(0,district)
    entry_dept.delete(0,END)
    entry_dept.insert(0,dept)


def action():
    for i in range(5):
        s=list[i]
        f=0
        if(f==0):
            for j in zilla:
                if(s==j):
                    global  district
                    district = s
                    f=1
                    break

        if(f==0):
            for j in s:
                if(j=='@'):
                    global  email
                    email=s
                    f=1
                    break;
        if(f==0):
            if (s.isdigit()):
                global mobile
                mobile=s
                f=1

        if(f==0):
            for j in departments:
                if(s==j):
                    f=1
                    global dept
                    dept=s
                    break

        if(f==0):
            global name
            name = s
            print(name)


def reset_it():
    entry_name.delete(0, END)
    entry_email.delete(0, END)
    entry_mobile.delete(0, END)
    entry_dist.delete(0, END)
    entry_dept.delete(0, END)
    list.clear()



topframe = Frame(root)
topframe.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)


#topframe
label1 = Label(topframe, text='Name',fg='green',font='Times 12',width=20,height=2)
label2 = Label(topframe, text='Email',fg='green',font='Times 12',width=20,height=2)
label3 = Label(topframe, text='Mobile',fg='green',font='Times 12',width=20,height=2)
label4 = Label(topframe, text='District',fg='green',font='Times 12',width=20,height=2)
label5 = Label(topframe, text='Department',fg='green',font='Times 12',width=20,height=2)

entry_name = Entry(topframe)
entry_email = Entry(topframe)
entry_mobile = Entry(topframe)
entry_dist = Entry(topframe)
entry_dept = Entry(topframe)

label1.grid(row=0, column=0,sticky=W+E)
entry_name.grid(row=0, column=1)

label2.grid(row=1, column=0,sticky=W+E)
entry_email.grid(row=1, column=1)

label3.grid(row=2, column=0,sticky=W+E)
entry_mobile.grid(row=2, column=1)

label4.grid(row=3, column=0,sticky=W+E)
entry_dist.grid(row=3, column=1)

label5.grid(row=4, column=0,sticky=W)
entry_dept.grid(row=4, column=1)




# bottom frame

save = Button(bottomframe, text='save', fg='green', font='Times=12',command=click_me,height=1,width=4)
exit = Button(bottomframe, text='exit', fg='red',font='Times=12', command=root.destroy,height=1,width=4)
reset=Button(bottomframe,text='Reset',fg='black',font='Times=12',command=reset_it,height=1,width=4)
save.pack(side=LEFT)
reset.pack(side=LEFT)
exit.pack(side=LEFT)

root.mainloop()
