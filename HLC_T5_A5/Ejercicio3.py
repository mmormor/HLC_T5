
class Individuo:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion

    def descripcion(self):
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y me dedico a {self.ocupacion}"

class Empleado(Individuo):
    def __init__(self, nombre, edad, ocupacion, compania):
        super().__init__(nombre, edad, ocupacion)
        self.compania = compania

    def informacion(self):
        return f"Hola, soy {self.nombre}, tengo {self.edad} años, trabajo como {self.ocupacion} en {self.compania}"

persona = Empleado("Alejandro", 20, "Informático", "Simire2")
print(persona.informacion())
