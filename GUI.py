import os
import pickle

class student:
    def __init__(self, a=0,b="",c="",d=0):
        self.roll=a
        self.name=b
        self.course=c
        self.fees=d
        
    def show(self):
        print(self.roll,'\t',self.name, '\t',self.course,'\t',self.fees)
      
        

from tkinter import*
window=Tk()
window.title("project")
window.geometry("500x200")

STUDENTS=[]

def showFees():
    global c
    x=int(Lb1.curselection()[0])
    if(x==0):
        fees=2000
        c='Python'
    if(x==1):
        fees=2500
        c='Perl'
    if(x==2):
        fees=3000
        c='C'
    if(x==3):
        fees=1500
        c='PHP'
    if(x==4):
        fees=4000
        c='SQL'
    s3.set(str(fees))
    

  
def studinfo():
    global STUDENTS
    r=int(s1.get())
    n=str(s2.get())
    f=int(s3.get())
    sobj=student(r,n,c,f)
    STUDENTS.append(sobj)
    s1.set("")
    s2.set("")
    s3.set("")
    
    
def SHOW():
    global STUDENTS
    print('ROLL','\t','NAME', '\t','COURSE','\t','FEES')
    for e in STUDENTS:
        e.show()

def SaveFile():
    global STUDENTS
    try:
        os.chdir('c:\students')
        fl1=open('nidhi.txt','wb')
        pickle.dump(STUDENTS,fl1)
        print('Data saved in nidhi.txt')
        fl1.close()
    except:
        print("File not found")

def LoadFile():
    global STUDENTS
    try:
        os.chdir('c:\students')
        fl1=open('nidhi.txt','rb')
        STUDENTS=pickle.load(fl1)
        print('Data loaded')
        fl1.close()
    except:
        print("File not found")
        
        
s1=StringVar()
s2=StringVar()
s1.set("0")
s2.set("I")

l1=Label(window, text="Enter Roll:")
e1=Entry(window, textvariable=s1)
l2=Label(window, text="Enter Name:")
e2=Entry(window, textvariable=s2)
l3=Label(window, text="Select Course:")
Lb1=Listbox(window, height=3, selectmode=SINGLE)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "SQL")
e4=Button(window, text="Fees", command=showFees)
s3=StringVar()
s3.set('0')
l4=Label(window, textvariable=s3)

b1=Button(window, text="Next", command=studinfo)
b2=Button(window, text="Show", command=SHOW)
b3=Button(window, text="Save", command=SaveFile)
b4=Button(window, text="Load", command=LoadFile)

l1.grid(row=0, column=0)
e1.grid(row=0, column=1)
b1.grid(row=0, column=2)
l2.grid(row=1, column=0)
e2.grid(row=1, column=1)
b2.grid(row=1, column=2)
l3.grid(row=2, column=0)
Lb1.grid(row=2, column=1)
e4.grid(row=3, column=0)
l4.grid(row=3, column=1)
b3.grid(row=2,column=2)
b4.grid(row=3, column=2)

window.mainloop()



