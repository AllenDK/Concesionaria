import subprocess
from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('Login')
root.geometry('700x400+300+300')
root.configure(bg="#fff")
root.resizable(False,False)

def signin():
    username=user.get()
    password=code.get()

    if username=='admin' and password=='1234':
        subprocess.Popen(["python3", "Menu.py"])
        root.withdraw()  # Oculta la ventana de inicio de sesión sin cerrarla
               
    elif username!='admin' and password!='1234':
        messagebox.showerror("Incorrecto", "Usuario y/o contraseña incorrectos")

    elif password!="1234":
        messagebox.showerror("Incorrecto","Contraseña incorrecta")

    elif username!="admin":
        messagebox.showerror("Incorrecto","Usuario incorrecto")


img = PhotoImage(file='Imagenes/Login.png')
Label(root, image=img, bg='white').place(x=50,y=50)

frame=Frame(root,width=350,heigh=350,bg='white')
frame.place(x=320,y=70)

heading=Label(frame,text='Sign in',fg='red',bg='white', font=('icrosoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

##################--------------------------------------------------------------
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Nombre de usuario')


user = Entry(frame,width=25,fg='black',border=0,bg="white", font=('icrosoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Nombre de usuario')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

##################--------------------------------------------------------------
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Contraseña')

code = Entry(frame,width=25,fg='black',border=0,bg="white", font=('icrosoft YaHei UI Light',11), show='*')
code.place(x=30,y=150)
code.insert(0,'Contraseña')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

##################--------------------------------------------------------------

Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='black',border=0,command=signin).place(x=35,y=204)


##################--------------------------------------------------------------


root.mainloop()