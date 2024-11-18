from tkinter import *
import tkinter.ttk as ttk

#Use class for window
class project(object):
    def __init__(self,win):
        win.title("Project-Part2")
        win.geometry("%dx%d+%d+%d" % (1000,800,50,50))
#Boxes definition
        self.f2="tahoma 14 normal"
        
        self.l1=Label(win,text="Video ID:",font=self.f2)
        self.l1.place(x=200,y=20)
        self.vi=IntVar()
        self.t1=Entry(win,textvariable=self.vi,font=self.f2,width=25)
        self.t1.place(x=300,y=20)

        self.l2=Label(win,text="Title:",font=self.f2)
        self.l2.place(x=200,y=60)
        self.ti=StringVar()
        self.t2=Entry(win,textvariable=self.ti,font=self.f2,width=25)
        self.t2.place(x=300,y=60)
        
        self.l3=Label(win,text="Description:",font=self.f2)
        self.l3.place(x=180,y=100)
        self.de=StringVar()
        self.t3=Entry(win,textvariable=self.de,font=self.f2,width=25)
        self.t3.place(x=300,y=100)        

        self.l4=Label(win,text="New Title:",font=self.f2)
        self.l4.place(x=200,y=180)
        self.nt=StringVar()
        self.t4=Entry(win,textvariable=self.nt,font=self.f2,width=25)
        self.t4.place(x=300,y=180)
        
        self.l5=Label(win,text="New Description:",font=self.f2)
        self.l5.place(x=150,y=220)
        self.nd=StringVar()
        self.t5=Entry(win,textvariable=self.nd,font=self.f2,width=25)
        self.t5.place(x=300,y=220)

#Functions   
    def fselect(self):
        pass
    def fdelete(self):
        pass
    def fupload(self):
        pass
    def fupdate(self):
        pass

#--------------------------------Main program -------------------------------------
win=Tk()
f1="tahoma 12 normal"

#Class object definition
proj=project(win)

#Buttons for doing queries
b1=Button(win,text="Select",font=f1,width=15,bg='light green',command=proj.fselect)
b1.place(x=600,y=20)

b2=Button(win,text="Delete",font=f1,width=15,bg='light green',command=proj.fdelete)
b2.place(x=600,y=60)

b3=Button(win,text="Upload",font=f1,width=15,bg='light green',command=proj.fupdate)
b3.place(x=600,y=100)

b4=Button(win,text="Update",font=f1,width=15,bg='light green',command=proj.fupload)
b4.place(x=600,y=220)

b5=Button(win,text="Exit",font=f1,width=15,bg='red',command=win.destroy)
b5.place(x=600,y=300)

#Nasrin Sheikhmoghaddasi
