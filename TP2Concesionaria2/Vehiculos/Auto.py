class Auto():
    def __init__ (self,marca,modelo,color,detalles):
        self.marca= marca
        self.modelo= modelo
        self.color= color
        self.detalles= detalles
        
    def __repr__(self):
        return str(self.__dict__)

    def __str__(self) -> str:
        return f'Detalles {self.detalles}'