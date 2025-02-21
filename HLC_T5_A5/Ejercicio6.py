coleccion_libros = []

class Libro:
    def __init__(self, nombre, escritor):
        self.nombre = nombre
        self.escritor = escritor

class Biblioteca:
    def añadir_libro(self, libro):
        coleccion_libros.append(libro)

    def listar_libros(self):
        for i, libro in enumerate(coleccion_libros, start=1):
            print(f"{i}. {libro.nombre} - {libro.escritor}")

mi_biblioteca = Biblioteca()
mi_biblioteca.añadir_libro(Libro("1984", "George Orwell"))
mi_biblioteca.añadir_libro(Libro("Cien Años de Soledad", "Gabriel García Márquez"))
mi_biblioteca.listar_libros()
