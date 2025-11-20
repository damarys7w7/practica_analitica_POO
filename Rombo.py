from FiguraGeometrica import FiguraGeometrica

class Rombo(FiguraGeometrica):
    def __init__(self, nombre):
        super().__init__(nombre)

    @property
    def diagonal_mayor(self) -> float:
        return self._diagonal_mayor
    
    @diagonal_mayor.setter
    def diagonal_mayor(self, diagonal_mayor: float):
        self._diagonal_mayor = diagonal_mayor

    @property
    def diagonal_menor(self) -> float:
        return self._diagonal_menor
    
    @diagonal_menor.setter
    def diagonal_menor(self, diagonal_menor: float):
        self._diagonal_menor = diagonal_menor

    def area(self) -> float:
        # Fórmula: (diagonal mayor * diagonal menor) / 2
        return (self.diagonal_mayor * self.diagonal_menor) / 2
