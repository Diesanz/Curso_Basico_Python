from capuchino import Capuchino
from descafeinado import Descafeinado

class Maquina:
    def __init__(self, numero, capacidad, lecheD, aguaD, azucarD):
        self.numero = numero
        self.capacidad = capacidad
        self.lecheD = lecheD
        self.aguaD = aguaD
        self.azucarD = azucarD
        self.cafes = []

    def disminuir_componentes(self, cafe):
        self.lecheD -= cafe.get_leche()
        self.aguaD -= cafe.get_agua()
        self.azucarD -= cafe.get_azucar()

    def agregar_cafe(self, cafe):
        if len(self.cafes) < self.capacidad:
            self.disminuir_componentes(cafe)
            self.cafes.append(cafe)
            print(f"Se ha agregado un {cafe.getTipo()} a la máquina.")
        else:
            print("La máquina está a su máxima capacidad.")

    def mostrar_estado(self):
        print(f"Máquina {self.numero} - Capacidad: {self.capacidad}")
        print(f"Leche disponible: {self.lecheD}L, Agua disponible: {self.aguaD}L, Azúcar disponible: {self.azucarD}g")
        print(f"Cafés en la máquina: {len(self.cafes)}")
        for cafe in self.cafes:
            cafe.informacion()

capuchino = Capuchino("0.15L", "0.15L", "2g", ["sucralosa"], "grande")
descafeinado = Descafeinado("0.25L", "0.25L", "1g", ["stevia"], "mediano")

maquina = Maquina(1, 5, 10, 20, 100)
maquina.agregar_cafe(capuchino)
maquina.agregar_cafe(descafeinado)
maquina.mostrar_estado()