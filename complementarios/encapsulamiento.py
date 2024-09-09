
from claseBasica import Persona

class Empleado(Persona):
    def __init__(self, nombre, edad, correo, salario):
        super().__init__(nombre, edad, correo)
        self.__salario = salario
    
    def mostrar_detalles(self):
        super().mostrar_detalles()
        print(f"Salario: {self.__salario}")
    
    def get_salario(self):
        return self.__salario
    
    def set_salario(self, nuevo_salario):
        if nuevo_salario > 0:
            self.__salario = nuevo_salario
        else:
            print("El salario debe de ser positivo")

empleado1 = Empleado("Ana", 35, "ana@example.com", 50000)
empleado1.mostrar_detalles()
print(f"Salario actual: {empleado1.get_salario()}")
empleado1.set_salario(60000)
print(f"Nuevo salario: {empleado1.get_salario()}")
empleado1.mostrar_detalles()