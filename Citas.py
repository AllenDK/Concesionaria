import subprocess
from tkinter import Entry, Tk, Frame, Label, Button, PhotoImage

# Funciones personalizadas para cada botón
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
root.title('Citas')
root.geometry('1300x700')
root.configure(bg="gray")
root.resizable(False, False)

# Crear el fondo de la franja
frame_franja = Frame(root, width=1300, height=80, bg='red')  # Ajusta el tamaño y el color según tu diseño
frame_franja.pack()

# Frame para los botones
frame_botones = Frame(frame_franja, bg='red')
frame_botones.place(x=100, y=30)

# Crear el fondo de la franja gris
frame_franja_gris = Frame(root, bg='#4D4D4D')  # Ajusta el tamaño y el color según tu diseño
frame_franja_gris.pack(fill='x') # Esto expandirá el frame horizontalmente para ajustarse al ancho de la ventana

# Etiqueta con el texto "REFACCIONES" sobre la franja gris
label_refacciones = Label(frame_franja_gris, text="CITAS", bg='#4D4D4D', fg='white', font=('icrosoft YaHei UI Light',20,'bold'))
label_refacciones.pack(padx=20, pady=10, side="left")

# Crear el fondo de la 3ra franja
#frame_franja_gris = Frame(root, width=1300, height=350, bg='gray')  # Ajusta el tamaño y el color según tu diseño
#frame_franja_gris.pack()

##########################

# Textos para cada botón
button_texts = ["CITAS", "CATALOGO", "VENTAS", "REFACCIONES", "SEGURO", "CERRAR SESION"]

# Crear cinco botones horizontales con acciones personalizadas
for i in range(6):
    button = Button(frame_botones, text=button_texts[i], command=actions[i], bg='gray', fg='white')
    button.pack(side="left", padx=30, pady=5)

img = PhotoImage(file='Imagenes/Logo.png')
Label(root, image=img, bg='red').place(x=10, y=10)  # Coloca la imagen en la esquina superior izquierda

root.mainloop()