from claseBasica import Persona

class Gerente(Persona):
    def __init__(self, nombre, edad, correo, departamento):
        super().__init__(nombre, edad, correo)
        self.departamento = departamento
    
    def mostrar_detalles(self):
        super().mostrar_detalles()
        print(f"Departamento: {self.departamento}")

gerente1 = Gerente("Carlos", 40, "carlos@example.com", "Ventas")
gerente1.mostrar_detalles()