class Individuo:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion

    def presentacion(self):
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y trabajo como {self.ocupacion}."

persona = Individuo("Ana", 28, "Ingeniera")
print(persona.presentacion())
