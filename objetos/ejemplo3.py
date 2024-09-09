class GrupoAnimal:
    x = 0
    nombre = ' '
    
    def __init__(self,nombre):
       self.nombre = nombre
       print(self.nombre, 'construido')

    def grupo(self):
        self.x = self.x+1
        print(self.nombre,'recuento grupal',self.x)


s = GrupoAnimal("Sally")
j = GrupoAnimal("Jim")

s.grupo()
j.grupo()
s.grupo()

