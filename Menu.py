import subprocess
from tkinter import W, Entry, StringVar, Tk, Frame, Label, Button, PhotoImage, ttk

def action_1():
    subprocess.Popen(["python3", "Citas.py"])
    root.withdraw()

def action_2():
    subprocess.Popen(["python3", "Catalogo.py"])
    root.withdraw()

def action_3():
    subprocess.Popen(["python3", "Ventas.py"])
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
root.geometry('1200x400+150+150')
root.configure(bg="gray")
root.resizable(False, False)

# Crear el fondo de la franja
frame_franja = Frame(root, width=1700, height=80, bg='red')
frame_franja.pack()

# Etiqueta de texto sobre la franja gris
label_nombre = Label(frame_franja, text="Concesionaria Dokaebi's", bg='red', fg='black', font=('Arial', 45, 'bold'))
label_nombre.place(relx=0.5, rely=0.5, anchor='center')

# Crear el fondo de la 3ra franja
frame_franja_gris_1 = Frame(root, width=1200, height=400, bg='gray')
frame_franja_gris_1.pack()

# Agregar la imagen como fondo usando un Label
image_label = Label(frame_franja_gris_1, width=1507, height=687, bg='red')
image_label.place(x=-20, y=-120)

img = PhotoImage(file='Imagenes/Menu.png')
image_label.img = img  # Mantén una referencia al objeto PhotoImage para evitar que sea eliminado por el recolector de basura
image_label.config(image=img)

# Crear los botones y posicionarlos sobre el Label
buttons = []

# Textos para cada botón
button_texts = ["CITAS", "CATALOGO", "VENTAS", "REFACCIONES", "SEGURO", "CERRAR SESION"]

# Configuración de las filas y columnas
button_width = 180
button_height = 50
button_padding_x = 30
button_padding_y = 100

# Obtener el ancho de la ventana principal
window_width = frame_franja_gris_1.winfo_reqwidth()

# Crear dos filas de tres botones cada una
for i in range(2):
    for j in range(3):
        index = i * 3 + j
        button = Button(frame_franja_gris_1, text=button_texts[index], command=actions[index], bg='gray', fg='black', font=('Arial', 15, 'bold'))
        x_position = (window_width - 3 * button_width - 2 * button_padding_x) / 2 + j * (button_width + button_padding_x)
        y_position = (i * (button_height + button_padding_y)) + button_padding_y
        button.place(x=x_position, y=y_position, width=button_width, height=button_height)
        button.lift()
        buttons.append(button)

img1 = PhotoImage(file='Imagenes/Logo.png')
Label(root, image=img1, bg='red').place(x=10, y=10)

root.mainloop()
