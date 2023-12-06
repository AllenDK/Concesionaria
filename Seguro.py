import subprocess
from tkinter import Entry, Tk, Frame, Label, Button, PhotoImage, ttk, StringVar, messagebox, filedialog

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

def guardar_ticket():
    # Obtener la información necesaria para el ticket
    detalles_seguro = f"Seguro: {año_combobox_var.get()}, Tipo de Seguro: {modelo_combobox_var.get()}"
    info_personal = "\n".join([f"{label} {entry.get()}" for label, entry in zip(labels_info_personal, info_entries)])
    etapa_compra = f"Tipo de compra: {etapa_compra_combobox.get()}"
    
    # Formatear el ticket
    ticket = f"DETALLES DEL SEGURO\n{detalles_seguro}\n\nINFORMACION PERSONAL\n{info_personal}\n{etapa_compra}"

    # Guardar el ticket en un archivo
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(ticket)

        # Mostrar un mensaje de éxito
        messagebox.showinfo("Ticket de Venta", f"Ticket guardado exitosamente en:\n{file_path}")

def mostrar_ticket():
    # Obtener la información necesaria para el ticket
    detalles_seguro = f"Seguro: {año_combobox_var.get()}, Tipo de Seguro: {modelo_combobox_var.get()}"
    info_personal = "\n".join([f"{label} {entry.get()}" for label, entry in zip(labels_info_personal, info_entries)])
    etapa_compra = f"Tipo de compra: {etapa_compra_combobox.get()}"
    
    # Formatear el ticket
    ticket = f"DETALLES DEL SEGURO\n{detalles_seguro}\n\nINFORMACION PERSONAL\n{info_personal}\n{etapa_compra}"

    # Mostrar el ticket en una ventana de mensaje
    messagebox.showinfo("Ticket de Venta", ticket)

# Lista de funciones para cada botón
actions = [action_1, action_2, action_3, action_4, action_5, action_6]

root = Tk()
root.title('Ventas Seguro')
root.geometry('1000x500')
root.configure(bg="gray")
root.resizable(False, False)

# Crear el fondo de la franja
frame_franja = Frame(root, width=1300, height=80, bg='red')  # Ajusta el tamaño y el color según tu diseño
frame_franja.pack()

# Frame para los botones
frame_botones = Frame(frame_franja, bg='red')
frame_botones.place(x=100, y=30)

# Crear el fondo de la franja gris
frame_franja_gris = Frame(root, bg='#4D4D4D')
frame_franja_gris.pack(fill='x') #expandir a lo ancho

# Etiqueta con el texto "COTIZACION" sobre la franja gris
label_refacciones = Label(frame_franja_gris, text="Ventas de seguro", bg='#4D4D4D', fg='white', font=('Microsoft YaHei UI Light',20,'bold'))
label_refacciones.pack(padx=20, pady=10, side="left")

# Crear el fondo de la 3ra franja
frame_franja_gris_1 = Frame(root,height=500, bg='gray')
frame_franja_gris_1.pack(fill='x')

# Etiqueta con el texto "DETALLES DEL SEGURO" sobre la franja gris_1
label_detalles = Label(frame_franja_gris_1, text="DETALLES DEL SEGURO", bg='gray', fg='white', font=('Microsoft YaHei UI Light', 14, 'bold'))
label_detalles.grid(row=0, column=0, pady=10, padx=20, sticky='w')

# Comboboxes para detalles del vehículo con etiquetas al lado izquierdo
labels_detalles_izquierdo = ["Seguro:", "Tipo de Seguro:"]
for i, label_text in enumerate(labels_detalles_izquierdo):
    label = Label(frame_franja_gris_1, text=label_text, bg='gray', fg='white')
    label.grid(row=i + 1, column=0, pady=5, padx=20, sticky='w')

# Combobox para "Seguro"
año_combobox_var = StringVar()
año_combobox = ttk.Combobox(frame_franja_gris_1, textvariable=año_combobox_var, values=["AVA", "AXA", "BBVA"], state="readonly")
año_combobox.grid(row=1, column=1, pady=5, padx=10, sticky='w')

# Combobox para "Tipo de Seguro"
modelo_combobox_var = StringVar()
modelo_combobox = ttk.Combobox(frame_franja_gris_1, textvariable=modelo_combobox_var, values=["Cobertura Basica", "Cobertura Media", "Cobertura Total "], state="readonly")
modelo_combobox.grid(row=2, column=1, pady=5, padx=10, sticky='w')

# Etiqueta con el texto "INFORMACION PERSONAL" sobre la franja gris_1
label_informacion_personal = Label(frame_franja_gris_1, text="INFORMACION PERSONAL", bg='gray', fg='white', font=('Microsoft YaHei UI Light', 14, 'bold'))
label_informacion_personal.grid(row=0, column=2, pady=10, padx=20, sticky='w')

# Textboxes y Comboboxes para información personal con etiquetas al lado izquierdo
labels_info_personal = ["Nombre:", "Apellido:", "Correo electrónico:", "Teléfono:"]
combobox_options = ["Cobertura Basica: $1500", "Cobertura Media: $3000", "Cobertura Total: $6000"]

info_entries = []
for i, label_text in enumerate(labels_info_personal):
    label = Label(frame_franja_gris_1, text=label_text, bg='gray', fg='white')
    label.grid(row=i + 1, column=2, pady=5, padx=20, sticky='w')

    entry = Entry(frame_franja_gris_1, width=20)
    entry.grid(row=i + 1, column=3, pady=5, padx=10, sticky='w')
    info_entries.append(entry)  # Agregar la entrada a la lista

# Etiqueta con el texto "Tipo de compra" sobre la franja gris_1
label_etapa_compra = Label(frame_franja_gris_1, text="Tipo de compra:", bg='gray', fg='white')
label_etapa_compra.grid(row=len(labels_info_personal) + 1, column=2, pady=5, padx=20, sticky='w')

# Combobox para la "Tipo de compra"
etapa_compra_combobox = ttk.Combobox(frame_franja_gris_1, values=combobox_options, state="readonly")
etapa_compra_combobox.grid(row=len(labels_info_personal) + 1, column=3, pady=5, padx=10, sticky='w')
info_entries.append(etapa_compra_combobox)  # Agregar el combobox a la lista

# Botón para guardar el ticket
guardar_ticket_button = Button(frame_franja_gris_1, text="Guardar Ticket", command=guardar_ticket, bg='gray', fg='white')
guardar_ticket_button.grid(row=len(labels_info_personal) + 2, column=2, pady=10, padx=20, sticky='w')

# Botón para mostrar el ticket
mostrar_ticket_button = Button(frame_franja_gris_1, text="Mostrar Ticket", command=mostrar_ticket, bg='gray', fg='white')
mostrar_ticket_button.grid(row=len(labels_info_personal) + 2, column=3, pady=10, padx=20, sticky='w')

# Textos para cada botón
button_texts = ["CITAS", "CATALOGO", "VENTAS", "REFACCIONES", "SEGURO", "CERRAR SESION"]

# Crear cinco botones horizontales con acciones personalizadas
for i in range(6):
    button = Button(frame_botones, text=button_texts[i], command=actions[i], bg='gray', fg='white')
    button.pack(side="left", padx=30, pady=5)

img = PhotoImage(file='Imagenes/Logo.png')
Label(root, image=img, bg='red').place(x=10, y=10)  # Coloca la imagen en la esquina superior izquierda

root.mainloop()
