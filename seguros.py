import tkinter as tk
from tkinter import ttk, messagebox

class VentaSegurosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Venta de Seguros")

        # Frame para la barra del menú (en rojo)
        self.frame_menu = tk.Frame(root, bg="red")
        self.frame_menu.pack(fill=tk.X)

        self.tipo_cobertura = tk.StringVar()

        # Sección de selección de cobertura
        tk.Label(self.frame_menu, text="Selecciona el tipo de cobertura:", bg="red", fg="white").pack(pady=10)

        opciones_cobertura = ["Cobertura Básica", "Cobertura Media", "Cobertura Total"]
        for opcion in opciones_cobertura:
            tk.Radiobutton(self.frame_menu, text=opcion, variable=self.tipo_cobertura, value=opcion, bg="red", fg="white").pack()

        # Frame para la parte inferior (en gris)
        self.frame_inferior = tk.Frame(root, bg="lightgray")
        self.frame_inferior.pack(fill=tk.BOTH, expand=True)

        # Sección de ingreso de datos del cliente
        tk.Label(self.frame_inferior, text="\nDatos del Cliente:").pack(pady=10)

        tk.Label(self.frame_inferior, text="Nombre:").pack()
        self.entry_nombre = tk.Entry(self.frame_inferior)
        self.entry_nombre.pack()

        tk.Label(self.frame_inferior, text="Teléfono:").pack()
        self.entry_telefono = tk.Entry(self.frame_inferior)
        self.entry_telefono.pack()

        # Botones para mostrar precios y generar ticket
        tk.Button(self.frame_inferior, text="Mostrar Precios", command=self.mostrar_precios).pack(pady=10)
        tk.Button(self.frame_inferior, text="Generar Ticket", command=self.generar_ticket).pack(pady=10)

        # Treeview para mostrar la lista de precios
        self.treeview_precios = ttk.Treeview(self.frame_inferior, columns=("Tipo", "Precio"), show="headings")
        self.treeview_precios.heading("Tipo", text="Tipo")
        self.treeview_precios.heading("Precio", text="Precio")
        self.treeview_precios.pack(side=tk.RIGHT, padx=20)

        # Canvas para mostrar el ticket
        self.canvas_ticket = tk.Canvas(self.frame_inferior, width=300, height=400, bg="white")
        self.canvas_ticket.pack(side=tk.RIGHT, padx=20)

    def mostrar_precios(self):
        tipo_cobertura_seleccionada = self.tipo_cobertura.get()

        if tipo_cobertura_seleccionada:
            precios = self.obtener_precios(tipo_cobertura_seleccionada)
            self.mostrar_precios_en_treeview(precios)
        else:
            messagebox.showwarning("Error", "Por favor, selecciona un tipo de cobertura.")

    def generar_ticket(self):
        tipo_cobertura_seleccionada = self.tipo_cobertura.get()
        nombre_cliente = self.entry_nombre.get()
        telefono_cliente = self.entry_telefono.get()

        if tipo_cobertura_seleccionada and nombre_cliente and telefono_cliente:
            precios = self.obtener_precios(tipo_cobertura_seleccionada)
            mensaje = f"Ticket de Venta:\n\n"
            mensaje += f"Precios para {tipo_cobertura_seleccionada}:\n"

            total_precio = 0

            for tipo, precio in precios.items():
                mensaje += f"{tipo}: ${precio}\n"
                total_precio += precio

            mensaje += f"\nTotal: ${total_precio}\n"
            mensaje += f"\nDatos del Cliente:\nNombre: {nombre_cliente}\nTeléfono: {telefono_cliente}"

            self.limpiar_canvas(self.canvas_ticket)
            self.dibujar_texto_en_canvas(self.canvas_ticket, mensaje)
        else:
            messagebox.showwarning("Error", "Por favor, completa todos los campos.")

    def mostrar_precios_en_treeview(self, precios):
        total_precio = 0

        self.treeview_precios.delete(*self.treeview_precios.get_children())

        for tipo, precio in precios.items():
            self.treeview_precios.insert("", "end", values=(tipo, f"${precio}"))
            total_precio += precio

        self.treeview_precios.insert("", "end", values=("Total", f"${total_precio}"))

    def obtener_precios(self, tipo_cobertura):
        # Simula precios de seguros (puedes ajustar estos valores según tus necesidades)
        if tipo_cobertura == "Cobertura Básica":
            return {"Responsabilidad Civil": 500, "Daños a Terceros": 700}
        elif tipo_cobertura == "Cobertura Media":
            return {"Responsabilidad Civil": 800, "Daños a Terceros": 1000, "Robo Parcial": 1200}
        elif tipo_cobertura == "Cobertura Total":
            return {"Responsabilidad Civil": 1200, "Daños a Terceros": 1500, "Robo Total": 2000}

    def limpiar_canvas(self, canvas):
        canvas.delete("all")

    def dibujar_texto_en_canvas(self, canvas, texto):
        canvas.create_text(10, 10, anchor="nw", text=texto, font=("Arial", 10), fill="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = VentaSegurosApp(root)
    root.mainloop()

