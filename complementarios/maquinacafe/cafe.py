class Cafe:
    def __init__(self, leche, agua, azucar, edulcorante, tamano):
        self.leche = leche
        self.agua = agua
        self.azucar = azucar
        self.edulcorante = edulcorante
        self.tamano = tamano
    
    def informacion(self):
        print(f"Café: {self.tamano}, Azúcar: {self.azucar}, Leche: {self.leche}, Agua: {self.agua}, Edulcorantes: {self.edulcorante}")

    def get_leche(self):
        return float(self.leche.rstrip('L'))

    def get_agua(self):
        return float(self.agua.rstrip('L'))

    def get_azucar(self):
        return float(self.azucar.rstrip('g'))