from claseBasica import Persona

class Empleado(Persona):
    def __init__(self, nombre, edad, correo, salario):
        super().__init__(nombre, edad, correo)
        self.salario = salario
    
    def mostrar_detalles(self):
        super().mostrar_detalles()
        print(f"Salario: {self.salario}")

empleado1 = Empleado("Ana", 35, "ana@example.com", 50000)
empleado1.mostrar_detalles()
    