class Individuo:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion

    def descripcion(self):
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y me dedico a {self.ocupacion}"

class Alumno(Individuo):
    def __init__(self, nombre, edad, ocupacion, nivel):
        super().__init__(nombre, edad, ocupacion)
        self.nivel = nivel

    def descripcion(self):
        return f"Hola, soy {self.nombre}, tengo {self.edad} años, me dedico a {self.ocupacion} y curso {self.nivel}"

persona = Alumno("Alejandro", 20, "Informática", "SMR")
print(persona.descripcion())
