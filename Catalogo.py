import subprocess
from tkinter import Entry, Tk, Frame, Label, Button, PhotoImage

# Funciones personalizadas para cada botón
def action_1():
    subprocess.Popen(["python3", "CompraAuto.py"])
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
root.title('Catalogo')
root.geometry('1300x700')
root.configure(bg="#fff")
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
label_refacciones = Label(frame_franja_gris, text="CATALOGO", bg='#4D4D4D', fg='white', font=('icrosoft YaHei UI Light',20,'bold'))
label_refacciones.pack(padx=20, pady=10, side="left")

# Crear el fondo de la 3ra franja
frame_franja_gris = Frame(root, width=1300, height=350, bg='gray')  # Ajusta el tamaño y el color según tu diseño
frame_franja_gris.pack()

# Crear el fondo de la 4ta franja
frame_franja_gris = Frame(root, bg='#4D4D4D')
frame_franja_gris.pack(fill='both', expand=True)

##########################

# Etiqueta con el texto "Cotizacion Rapida" sobre la franja gris
label_Cotizacion = Label(frame_franja_gris, text="Cotizacion", bg='#4D4D4D', fg='white', font=('Microsoft YaHei UI Light', 20, 'bold'))
label_Cotizacion.pack(side="top", pady=20, anchor="center")

# Textos para cada botón
button_texts = ["AUTOS NUEVOS", "CATALOGO", "COTIZACION", "REFACCIONES", "SEGURO", "CERRAR SESION"]

# Crear cinco botones horizontales con acciones personalizadas
for i in range(6):
    button = Button(frame_botones, text=button_texts[i], command=actions[i], bg='gray', fg='white')
    button.pack(side="left", padx=20, pady=5)


###Cuadros de texto
# Agregar etiquetas y cuadros de texto para la información
labels = ["Nombre:", "Apellido:", "Teléfono:", "Email:", "Modelo:"]
text_entries = []

for i in range(5):
    label = Label(frame_franja_gris, text=labels[i], bg='#4D4D4D', fg='white')
    label.pack(side="left", padx=5, pady=5)

    entry = Entry(frame_franja_gris, width=20)
    entry.pack(side="left", padx=5, pady=5)

    text_entries.append(entry)

# Función para imprimir la información cuando se presiona el botón
def print_info():
    for i in range(5):
        print(f"{labels[i]} {text_entries[i].get()}")

# Botón para guardar la información
save_button = Button(frame_franja_gris, text="Guardar Información", command=print_info, bg='gray', fg='white')
save_button.pack(side="left", pady=10, padx=20)


img = PhotoImage(file='Imagenes/principal1.png')
Label(root, image=img, bg='red').place(x=10, y=10)  # Coloca la imagen en la esquina superior izquierda

root.mainloop()