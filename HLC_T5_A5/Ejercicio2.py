class Personas:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
    def presentar(self):
        return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.profesion}"
class Estudiante(Personas):
    def __init__(self, nombre, edad, profesion, grado):
        super().__init__(nombre, edad, profesion)
        self.grado = grado
    def presentar(self):
        return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años, soy {self.profesion} y estudio {self.grado}"
p = Estudiante('Alejandro', 20, 'Informático', 'SMR')
print(p.presentar())
