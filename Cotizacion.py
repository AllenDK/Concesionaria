import subprocess
from tkinter import Entry, Tk, Frame, Label, Button, PhotoImage, ttk, StringVar

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
root.title('Cotizacion')
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
frame_franja_gris = Frame(root, bg='#4D4D4D')
frame_franja_gris.pack(fill='x') # Esto expandirá el frame horizontalmente para ajustarse al ancho de la ventana

# Etiqueta con el texto "COTIZACION" sobre la franja gris
label_refacciones = Label(frame_franja_gris, text="COTIZACION", bg='#4D4D4D', fg='white', font=('icrosoft YaHei UI Light',20,'bold'))
label_refacciones.pack(padx=20, pady=10, side="left")

# Crear el fondo de la 3ra franja
frame_franja_gris_1 = Frame(root,height=500, bg='gray')
frame_franja_gris_1.pack(fill='x')


######### LO RELEVANTE A LOS TEXTBOX Y COMBOBOX
# Etiqueta con el texto "DETALLES DEL VEHICULO" sobre la franja gris_1
label_detalles = Label(frame_franja_gris_1, text="DETALLES DEL VEHICULO", bg='gray', fg='white', font=('Microsoft YaHei UI Light', 14, 'bold'))
label_detalles.grid(row=0, column=0, pady=10, padx=20, sticky='w')

# Comboboxes para detalles del vehículo con etiquetas al lado izquierdo
detalles_var1 = StringVar()
detalles_var2 = StringVar()

labels_detalles_izquierdo = ["Año:", "Modelo:"]
for i, label_text in enumerate(labels_detalles_izquierdo):
    label = Label(frame_franja_gris_1, text=label_text, bg='gray', fg='white')
    label.grid(row=i + 1, column=0, pady=5, padx=20, sticky='w')

    combobox = ttk.Combobox(frame_franja_gris_1, textvariable=detalles_var1 if i == 0 else detalles_var2, values=["Opción 1", "Opción 2", "Opción 3"])
    combobox.grid(row=i + 1, column=1, pady=5, padx=10, sticky='w')

# Etiqueta con el texto "INFORMACION PERSONAL" sobre la franja gris_1
label_informacion_personal = Label(frame_franja_gris_1, text="INFORMACION PERSONAL", bg='gray', fg='white', font=('Microsoft YaHei UI Light', 14, 'bold'))
label_informacion_personal.grid(row=0, column=2, pady=10, padx=20, sticky='w')

# Textboxes y Comboboxes para información personal con etiquetas al lado izquierdo
labels_info_personal = ["Nombre:", "Apellido:", "Correo electronico:", "Telefono:", "Etapa de compra:"]
combobox_options = ["Opción 1", "Opción 2", "Opción 3"]

for i, label_text in enumerate(labels_info_personal):
    label = Label(frame_franja_gris_1, text=label_text, bg='gray', fg='white')
    label.grid(row=i + 1, column=2, pady=5, padx=20, sticky='w')

    if i == len(labels_info_personal) - 1:  # Último elemento
        combobox_var = StringVar()
        combobox = ttk.Combobox(frame_franja_gris_1, textvariable=combobox_var, values=combobox_options)
        combobox.grid(row=i + 1, column=3, pady=5, padx=10, sticky='w')
    else:
        entry = Entry(frame_franja_gris_1, width=20)
        entry.grid(row=i + 1, column=3, pady=5, padx=10, sticky='w')
###########################


# Crear el fondo de la 4ta franja
frame_franja_gris_2 = Frame(root, bg='#4D4D4D')
frame_franja_gris_2.pack(fill='both', expand=True)

# Textos para cada botón
button_texts = ["AUTOS NUEVOS", "CATALOGO", "COTIZACION", "REFACCIONES", "SEGURO", "CERRAR SESION"]

# Crear cinco botones horizontales con acciones personalizadas
for i in range(6):
    button = Button(frame_botones, text=button_texts[i], command=actions[i], bg='gray', fg='white')
    button.pack(side="left", padx=20, pady=5)


img = PhotoImage(file='Imagenes/principal1.png')
Label(root, image=img, bg='red').place(x=10, y=10)  # Coloca la imagen en la esquina superior izquierda

root.mainloop()