from cafe import Cafe

class Capuchino(Cafe):
    def __init__(self, leche, agua, azucar, edulcorante, tamano, tipo="capuchino"):
        super().__init__(leche, agua, azucar, edulcorante, tamano)
        self.tipo = tipo
    
    def informacion(self):
        super().informacion()
        print(f"tipo: {self.tipo}")

    def getTipo(self):
        return self.tipo
