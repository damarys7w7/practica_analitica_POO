from FiguraGeometrica import FiguraGeometrica
from math import pi
class Cilindro(FiguraGeometrica):
    def __init__(self, nombre):
        super().__init__(nombre)


    @property
    def radio(self) -> float:
        return self.radio
    
    @radio.setter
    def radio(self,radio:float):
        self._radio =radio

    @property
    def altura(self) -> float:
        return self.altura
    @altura.setter
    def altura(self,altura: float):
        return self.altura
    
    def area (self):
        return 2*pi*self.radio(self.radio*self.altura)
