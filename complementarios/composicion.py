from encapsulamiento import Empleado
from polimorfismo import Gerente    

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
    
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def mostrar_empleados(self):
        print(f"Empleados de {self.nombre}")
        for empleado in self.empleados:
            empleado.mostrar_detalles()

empresa1 = Empresa("TechCorp")
empleado1 = Empleado("Ana", 35, "ana@example.com", 50000)
empleado2 = Gerente("Carlos", 40, "carlos@example.com", "Ventas")

empresa1.agregar_empleado(empleado1)
empresa1.agregar_empleado(empleado2)
empresa1.mostrar_empleados()