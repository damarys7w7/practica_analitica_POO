from FiguraGeometrica import FiguraGeometrica
class Circulo (FiguraGeometrica):
    def __init__(self,radio):
        self.radio=radio

    def area (self):
        return 3.1416 * self.radio * self.radio