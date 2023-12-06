import subprocess
from tkinter import W, Entry, StringVar, Tk, Frame, Label, Button, PhotoImage, ttk

# Funciones personalizadas para cada botón
def action_1():
    subprocess.Popen(["python3", "Menu.py"])
    root.withdraw()

def action_2():
    subprocess.Popen(["python3", "Catalogo.py"])
    root.withdraw()

def action_3():
    subprocess.Popen(["python3", "Cotizacion.py"])
    root.withdraw()

def action_4():
    subprocess.Popen(["python3", "Refacciones.py"])
    root.withdraw()

def action_5():
    subprocess.Popen(["python3", "Seguro.py"])
    root.withdraw()

def action_6():
    subprocess.Popen(["python3", "Login.py"])
    root.withdraw()

# Lista de funciones para cada botón
actions = [action_1, action_2, action_3, action_4, action_5, action_6]

root = Tk()
root.title('Principal')
root.geometry('1506x700+150+150')
root.configure(bg="gray")
root.resizable(False, False)

# Crear el fondo de la franja
frame_franja = Frame(root, width=1700, height=80, bg='red')
frame_franja.pack()

# Crear el fondo de la franja gris
#frame_franja_gris = Frame(root, bg='#4D4D4D')
#frame_franja_gris.pack(fill='x')

# Etiqueta de texto sobre la franja gris
label_nombre = Label(frame_franja, text="Concesionaria Dokaebi's", bg='red', fg='black', font=('Arial', 45, 'bold'))
label_nombre.place(relx=0.5, rely=0.5, anchor='center')

# Crear el fondo de la 3ra franja
frame_franja_gris_1 = Frame(root, width=1507, height=687, bg='gray')
frame_franja_gris_1.pack()

# Textos para cada botón
button_texts = ["AUTOS NUEVOS", "CATALOGO", "COTIZACION", "REFACCIONES", "SEGURO", "CERRAR SESION"]

# Agregar la imagen como fondo usando un Label
image_label = Label(frame_franja_gris_1, width=1507, height=687, bg='red')
image_label.place(x=-3, y=0)

img = PhotoImage(file='Imagenes/Menu.png')
image_label.img = img  # Mantén una referencia al objeto PhotoImage para evitar que sea eliminado por el recolector de basura
image_label.config(image=img)

# Crear los botones y posicionarlos sobre el Label
buttons = []

for i in range(6):
    button = Button(frame_franja_gris_1, text=button_texts[i], command=actions[i], bg='gray', fg='white')
    button.place(x=10 + i * 150, y=10)  
    button.lift()  
    buttons.append(button)

img1 = PhotoImage(file='Imagenes/Logo.png')
Label(root, image=img1, bg='red').place(x=10, y=10)

root.mainloop()
