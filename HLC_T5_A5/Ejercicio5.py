import math

class FormaGeometrica:
    def __init__(self):
        pass

    def obtener_area(self):
        pass

class Esfera(FormaGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def obtener_area(self):
        return math.pi * (self.radio ** 2)

class Cuadrilatero(FormaGeometrica):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def obtener_area(self):
        return self.ancho * self.alto

figura1 = Esfera(5)
figura2 = Cuadrilatero(4, 6)

print(figura1.obtener_area())
print(figura2.obtener_area())
