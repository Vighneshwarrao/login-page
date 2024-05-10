from tkinter import *
from tkinter import messagebox
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="vighnesh",password="Idlisambar26!",database="data")
mycursor=mydb.cursor()
def validateLogin():
        #checking of user in database
        cmd="SELECT roll_no FROM CSMC WHERE roll_no=%s"
        mycursor.execute(cmd,(username.get(),))
        valid=mycursor.fetchall()
        if valid:
                #Ifuserfound
                cmd1="SELECT roll_no FROM CSMC WHERE roll_no=%s AND password=%s"
                check=(username.get(),password.get())
                mycursor.execute(cmd1,check)
                res=mycursor.fetchall()
                if res:
                        #validlogin
                        window1=Tk()
                        window1.title("LOGIN")
                        window1.geometry("500x150")
                        name=username.get()
                        l1=Label(window1,text=(f"{name}....YOU ARE A MEMBER OF CSM-C"),font=("Deja vu",15)).pack()
                else:
                        #invalid login
                        messagebox.showerror("LOGIN","INVALID PASSWORD")
        else:           
                #nouserfound
                messagebox.showerror("LOGIN",f"{username.get()} NOT FOUND.. TRY SIGNUP")
        return
def signup():
        #checking of user in database
        cmd="SELECT roll_no FROM CSMC WHERE roll_no=%s"
        mycursor.execute(cmd,(username.get(),))
        valid=mycursor.fetchall()
        if valid:
                 #MEMBER ALREADY EXISTS
                 messagebox.showerror("SIGNUP",f"{username.get()} EXISTS.. TRY LOGIN")
        else:
                #inserting data into database
                insrt="INSERT INTO CSMC(roll_no,password) VALUES(%s,%s)"
                val=(username.get(),password.get())
                mycursor.execute(insrt,val)
                #singupmsg
                messagebox.showinfo("SINGUP"," SignUp Sucessfull")
                mydb.commit()
#window
window = Tk()  
window.geometry('400x150')  
window.title('CSM-C login')

#username label and text entry box
usernameLabel = Label(window, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(window, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(window,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(window, textvariable=password, show='*').grid(row=1, column=1)

#login button
loginButton = Button(window, text="Login", command=validateLogin,bg='green',fg='white').grid(row=2, column=0)
#signup button
signupbutton=Button(window,text="Sign Up",command=signup,bg='orange',fg='white').grid(row=2,column=1)
window.mainloop()

