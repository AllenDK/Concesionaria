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
root.title('Catalogo')
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
label_refacciones = Label(frame_franja_gris, text="CATALOGO", bg='#4D4D4D', fg='white', font=('icrosoft YaHei UI Light',20,'bold'))
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
    button.pack(side="left", padx=20, pady=5)

img = PhotoImage(file='Imagenes/principal1.png')
Label(root, image=img, bg='red').place(x=10, y=10)  # Coloca la imagen en la esquina superior izquierda

############Honda
# Cargar la imagen del carro
img_carro = PhotoImage(file='Imagenes/Honda.png')

# Ajustar la medida de la imagen
factor_muestreo = 2  # Ajusta según sea necesario
img_carro = img_carro.subsample(factor_muestreo, factor_muestreo)


# Crear una etiqueta para mostrar la imagen
label_carro = Label(root, image=img_carro, bd=0, relief='flat', bg='gray')  
label_carro.place(x=0, y=150)  # Coloca la imagen en la esquina superior izquierda

# Datos ficticios del carro
Honda = {
    'Año': '2023',
    'Marca': 'Honda',
    'Modelo': 'Civic',
    'Versión': 'Sport',
    'Precio': '$200,000'
}

# Crear etiquetas para mostrar la información
y_pos = 340  # Ajusta la posición vertical según sea necesario

for key, value in Honda.items():
    label_info = Label(root, text=f"{key}: {value}", bg='gray', fg='black', font=('Arial', 12))
    label_info.place(x=10, y=y_pos)
    y_pos += 30  # Incrementa la posición vertical para la siguiente etiqueta

###########Scion
# Cargar la imagen del carro
img_carro1 = PhotoImage(file='Imagenes/Scion.png')

# Ajustar la medida de la imagen
factor_muestreo = 2  # Ajusta según sea necesario
img_carro1 = img_carro1.subsample(factor_muestreo, factor_muestreo)

# Crear una etiqueta para mostrar la imagen
label_carro1 = Label(root, image=img_carro1, bd=0, relief='flat', bg='gray')  
label_carro1.place(x=320, y=150)  # Coloca la imagen en la esquina superior izquierda

# Datos ficticios del carro
Scion = {
    'Año': '2016',
    'Marca': 'Toyota',
    'Modelo': 'Scion',
    'Versión': 'FR-S',
    'Precio': '$280,000'
}

# Crear etiquetas para mostrar la información
y_pos = 340  # Ajusta la posición vertical según sea necesario

for key, value in Scion.items():
    label_info1 = Label(root, text=f"{key}: {value}", bg='gray', fg='black', font=('Arial', 12))
    label_info1.place(x=320, y=y_pos)
    y_pos += 30  # Incrementa la posición vertical para la siguiente etiqueta

###########Nissan
# Cargar la imagen del carro
img_carro2 = PhotoImage(file='Imagenes/Nissan.png')

# Ajustar la medida de la imagen
factor_muestreo = 4  # Ajusta según sea necesario
img_carro2 = img_carro2.subsample(factor_muestreo, factor_muestreo)

# Crear una etiqueta para mostrar la imagen
label_carro2 = Label(root, image=img_carro2, bd=0, relief='flat', bg='gray')  
label_carro2.place(x=650, y=190)  # Coloca la imagen en la esquina superior izquierda

# Datos ficticios del carro
Nissan = {
    'Año': '2017',
    'Marca': 'Nissan',
    'Modelo': '370Z',
    'Versión': 'Nismo',
    'Precio': '$817,000'
}

# Crear etiquetas para mostrar la información
y_pos = 340  # Ajusta la posición vertical según sea necesario

for key, value in Nissan.items():
    label_info2 = Label(root, text=f"{key}: {value}", bg='gray', fg='black', font=('Arial', 12))
    label_info2.place(x=670, y=y_pos)
    y_pos += 30  # Incrementa la posición vertical para la siguiente etiqueta

###########Ranger
# Cargar la imagen del carro
img_carro3 = PhotoImage(file='Imagenes/Ranger.png')

# Ajustar la medida de la imagen
factor_muestreo = 1  # Ajusta según sea necesario
img_carro3 = img_carro3.subsample(factor_muestreo, factor_muestreo)

# Crear una etiqueta para mostrar la imagen
label_carro3 = Label(root, image=img_carro3, bd=0, relief='flat', bg='gray')  
label_carro3.place(x=950, y=170)  # Coloca la imagen en la esquina superior izquierda

# Datos ficticios del carro
Ranger = {
    'Año': '2023',
    'Marca': 'Ford',
    'Modelo': 'Bronco',
    'Versión': 'Sport',
    'Precio': '$1,000,000'
}

# Crear etiquetas para mostrar la información
y_pos = 340  # Ajusta la posición vertical según sea necesario

for key, value in Ranger.items():
    label_info3 = Label(root, text=f"{key}: {value}", bg='gray', fg='black', font=('Arial', 12))
    label_info3.place(x=1010, y=y_pos)
    y_pos += 30  # Incrementa la posición vertical para la siguiente etiqueta

root.mainloop()