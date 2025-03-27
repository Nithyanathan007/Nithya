from tkinter import *
from tkinter import messagebox
def login():
     username = entry.get()
     password =entry2.get()
     if username == 'welcome' and password == '123':
          messagebox.showinfo('sussesfully login')
          root.destroy()
          top = Tk()
          label4 = Label(top, text='welcome!')
     elif 
        messagebox.showinfo('invalid username or password') 
root=Tk()
root.configure(bg='white')
label1 = Label(root,text='Login Page', fg='red', font=('areal',20))

label1.place(x=500,y=20)
label2 = Label(root,text='username:', font=('Areal',20), fg='black')
label2.place(x=310, y=190)  
label3 = Label(root,text='password:', font=('Areal',20), fg='black')
label3.place(x=310, y=340) 
entry1 = Entry(root, font=('Areal', 15))
entry1.place(x=600, y=200)
entry2 = Entry(root, font=('areal', 15))
entry2.place(x=600, y=350)
button = Button(root, text ='Login', bg='blue', font=('Areal', 15), bd=5, command=login)
button.place(x=600, y=500)
root.mainloop() 