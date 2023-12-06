import subprocess
from tkinter import W, Entry, StringVar, Tk, Frame, Label, Button, PhotoImage, ttk

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
root.title('Refacciones')
root.geometry('1506x700+150+150')
root.configure(bg="gray")
root.resizable(False, False)

# Crear el fondo de la franja
frame_franja = Frame(root, width=1700, height=80, bg='red')
frame_franja.pack()

# Frame para los botones
frame_botones = Frame(frame_franja, bg='red')
frame_botones.place(x=100, y=30)

# Crear el fondo de la franja gris
frame_franja_gris = Frame(root, bg='#4D4D4D')
frame_franja_gris.pack(fill='x')

# Etiqueta con el texto "REFACCIONES" sobre la franja gris
label_refacciones = Label(frame_franja_gris, text="Refacciones", bg='#4D4D4D', fg='white', font=('Microsoft YaHei UI Light', 20, 'bold'))
label_refacciones.pack(padx=20, pady=10, side="left")

# Crear el fondo de la 3ra franja
frame_franja_gris_1 = Frame(root,height=350, bg='gray')
frame_franja_gris_1.pack(fill='x')

#########     DETALLES DE VEHICULO

# Etiqueta con el texto "Detalles del Vehículo"
label_detalles = Label(frame_franja_gris_1, text="Detalles del Vehículo", bg='gray', fg='white', font=('Microsoft YaHei UI Light', 16, 'bold'))
label_detalles.grid(row=0, column=0, columnspan=1, pady=10)

# Cuadros de texto para los detalles
detalles_entries = []
detalles_combobox_options = {
    "Año": ["2023", "2022", "2021", "2020"],
    "Marca": ["Toyota", "Ford", "Chevrolet", "Honda"],
    "Modelo": ["Camry", "F-150", "Silverado", "Civic"],
    "Version": ["SE", "XLT", "LTZ", "Touring"]
}

for i, (label_text, options) in enumerate(detalles_combobox_options.items()):
    label = Label(frame_franja_gris_1, text=label_text, bg='gray', fg='white', font=('Microsoft YaHei UI Light', 13, 'bold'))
    label.grid(row=i + 1, column=0, padx=5, pady=5, sticky='e')

    combobox = ttk.Combobox(frame_franja_gris_1, values=options, state="readonly")
    combobox.grid(row=i + 1, column=1, padx=5, pady=5)

    detalles_entries.append(combobox)

# Cuadros de entrada para VIN# y Refaccion Requerida
vin_entry = Entry(frame_franja_gris_1, width=20)
vin_entry.grid(row=len(detalles_combobox_options) + 1, column=1, padx=5, pady=5)
detalles_entries.append(vin_entry)

refaccion_entry = Entry(frame_franja_gris_1, width=20)
refaccion_entry.grid(row=len(detalles_combobox_options) + 2, column=1, padx=5, pady=5)
detalles_entries.append(refaccion_entry)

# Etiquetas para los cuadros de entrada
vin_label = Label(frame_franja_gris_1, text="VIN#:", bg='gray', fg='white', font=('Microsoft YaHei UI Light', 13, 'bold'))
vin_label.grid(row=len(detalles_combobox_options) + 1, column=0, padx=5, pady=5, sticky='e')

refaccion_label = Label(frame_franja_gris_1, text="Refaccion Requerida:", bg='gray', fg='white', font=('Microsoft YaHei UI Light', 13, 'bold'))
refaccion_label.grid(row=len(detalles_combobox_options) + 2, column=0, padx=5, pady=5, sticky='e')

# Agregar una imagen en el lado derecho
img_vehiculo = PhotoImage(file='Imagenes/Refacciones.png')
label_vehiculo = Label(frame_franja_gris_1, image=img_vehiculo, bg='gray')
label_vehiculo.grid(row=1, column=2, rowspan=len(detalles_entries), padx=200)

############

# Crear el fondo de la 4ta franja
frame_franja_gris_2 = Frame(root, bg='#4D4D4D')
frame_franja_gris_2.pack(fill='both', expand=True)

# Textos para cada botón
button_texts = ["CITAS", "CATALOGO", "VENTAS", "REFACCIONES", "SEGURO", "CERRAR SESION"]

# Crear cinco botones horizontales con acciones personalizadas
for i in range(6):
    button = Button(frame_botones, text=button_texts[i], command=actions[i], bg='gray', fg='white')
    button.pack(side="left", padx=20, pady=5)

img1 = PhotoImage(file='Imagenes/Logo.png')
Label(root, image=img1, bg='red').place(x=10, y=10)

#img = PhotoImage(file='Imagenes/Menu.png')
#Label(root, width=1507, height=349, image=img, bg='red').place(x=-1, y=135)

root.mainloop()