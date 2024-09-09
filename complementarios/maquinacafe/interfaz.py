import tkinter as tk
from tkinter import messagebox
from capuchino import Capuchino
from descafeinado import Descafeinado
from maquina import Maquina

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Máquina de Café")

        self.maquina = Maquina(1, 5, 10, 20, 100)

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.create_widgets()

    def create_widgets(self):
        self.label_tipo = tk.Label(self.frame, text="Tipo de Café:")
        self.label_tipo.grid(row=0, column=0)

        self.tipo_var = tk.StringVar()
        self.tipo_var.set("capuchino")
        self.option_tipo = tk.OptionMenu(self.frame, self.tipo_var, "capuchino", "descafeinado")
        self.option_tipo.grid(row=0, column=1)

        self.label_tamano = tk.Label(self.frame, text="Tamaño:")
        self.label_tamano.grid(row=1, column=0)

        self.tamano_var = tk.StringVar()
        self.tamano_var.set("mediano")
        self.option_tamano = tk.OptionMenu(self.frame, self.tamano_var, "pequeño", "mediano", "grande")
        self.option_tamano.grid(row=1, column=1)

        self.boton_agregar = tk.Button(self.frame, text="Agregar Café", command=self.agregar_cafe)
        self.boton_agregar.grid(row=2, columnspan=2)

        self.boton_estado = tk.Button(self.frame, text="Mostrar Estado", command=self.mostrar_estado)
        self.boton_estado.grid(row=3, columnspan=2)

    def agregar_cafe(self):
        tipo = self.tipo_var.get()
        tamano = self.tamano_var.get()

        if tipo == "capuchino":
            cafe = Capuchino("0.15L", "0.15L", "2g", ["sucralosa"], tamano)
        elif tipo == "descafeinado":
            cafe = Descafeinado("0.25L", "0.25L", "1g", ["stevia"], tamano)
        
        self.maquina.agregar_cafe(cafe)
        messagebox.showinfo("Información", f"Se ha agregado un {tipo} {tamano} a la máquina.")

    def mostrar_estado(self):
        estado = f"Máquina {self.maquina.numero} - Capacidad: {self.maquina.capacidad}\n"
        estado += f"Leche disponible: {self.maquina.lecheD}L, Agua disponible: {self.maquina.aguaD}L, Azúcar disponible: {self.maquina.azucarD}g\n"
        estado += f"Cafés en la máquina: {len(self.maquina.cafes)}\n"
        for cafe in self.maquina.cafes:
            estado += f"{cafe.get_tipo()} {cafe.tamano}\n"

        messagebox.showinfo("Estado de la Máquina", estado)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
