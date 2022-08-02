from tkinter import*
from tkinter import ttk
from time import strftime
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
import pymysql

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1200x668+0+0")

        mypass = "jahnvi"
        mydatabase="libmanagement"

        con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
        cur = con.cursor()

        # =======================TitleLabel======================================================================
        lbltitle=Label(self.root,text="BOOK MANAGEMENT SYSTEM",bg="white",fg="crimson",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        def time(): 
            string = strftime('%I:%M:%S %p') 
            lbl.config(text = string) 
            lbl.after(1000, time) 
        
        lbl = Label(lbltitle, font = ('times new roman',15, 'bold'),background = 'purple',foreground = 'white') 
        lbl.place(x=0,y=0,width=150) 
        time() 

        
        self.m=Message(self.root, text="WELCOME TO THE LIBRARY",width=700,font=('times new roman',20,'bold italic'),fg='crimson',bg='cyan')
        self.m.pack(padx = 15, pady = 15)

        Messageframe=Frame(self.root,bd=20,padx=20,relief=RIDGE)
        Messageframe.place(x=0,y=420,width=1200,height=90)
        self.m=Message(Messageframe, text="Please select a button",width=700,font=('times new roman',20,'bold'),fg='crimson',bg='cyan')
        self.m.pack()

        ButtonFrame=Frame(self.root,bd=20,padx=20,relief=RIDGE)
        ButtonFrame.place(x=0,y=520,width=1200,height=80)

        btn1=Button(ButtonFrame,text="Add Book Details",command=addBook,width=16,font=("arial",12,"bold"),bg='crimson',fg='white')
        btn1.pack(fill=X,expand=TRUE,side=LEFT)
        
        btn2=Button(ButtonFrame,text="Delete Book",command=delete,width=16,font=("arial",12,"bold"),bg='crimson',fg='white')
        btn2.pack(fill=X,expand=TRUE,side=LEFT)

        btn3=Button(ButtonFrame,text="View list of Books",command=View,width=16,font=("arial",12,"bold"),bg='crimson',fg='white')
        btn3.pack(fill=X,expand=TRUE,side=LEFT)

        btn4=Button(ButtonFrame,text="Issue Book",command=issueBook,width=16,font=("arial",12,"bold"),bg='crimson',fg='white')
        btn4.pack(fill=X,expand=TRUE,side=LEFT)

        btn5=Button(ButtonFrame,text="Return Book",command=returnBook,width=16,font=("arial",12,"bold"),bg='crimson',fg='white')
        btn5.pack(fill=X,expand=TRUE,side=LEFT)

        btn2=Button(ButtonFrame,text="Exit",width=16,font=("arial",12,"bold"),bg='crimson',fg='white',command=self.root.destroy)
        btn2.pack(fill=X,expand=TRUE,side=LEFT)



        
if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()