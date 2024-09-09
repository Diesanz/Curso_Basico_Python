class Persona:
    def __init__(self,nombre,edad,correo):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
    
    def mostrar_detalles(self):
         print(f"Nombre: {self.nombre}, Edad: {self.edad}, Correo: {self.correo}")

persona1 = Persona("Juan", 28, "juan@example.com")
persona1.mostrar_detalles()