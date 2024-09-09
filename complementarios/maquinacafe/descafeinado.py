from cafe import Cafe

class Descafeinado(Cafe):
    def __init__(self, leche, agua, azucar, edulcorante, tamano, tipo="descafeinado"):
        super().__init__(leche, agua, azucar, edulcorante, tamano)
        self.tipo = tipo
    
    def informacion(self):
        super().informacion()
        print(f"Tipo: {self.tipo}")

    def getTipo(self):
        return self.tipo
    
