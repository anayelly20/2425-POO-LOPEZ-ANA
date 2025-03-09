import json

# Clase libro
class Libro:
    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str, prestado=False):
        self.info = (titulo, autor)  # Tupla inmutable
        self.categoria = categoria
        self.isbn = isbn
        self.prestado = prestado

    def to_dict(self):
        return {
            "titulo": self.info[0],
            "autor": self.info[1],
            "categoria": self.categoria,
            "isbn": self.isbn,
            "prestado": self.prestado
        }

    def __str__(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f'Título: {self.info[0]}, Autor: {self.info[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}, Estado: {estado}'

# Clase usuario
class Usuario:
    def __init__(self, nombre: str, user_id: str):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista de ISBNs

    def __str__(self):
        return f'Usuario: {self.nombre}, ID: {self.user_id}'

# Clase biblioteca
class Biblioteca:
    def __init__(self, archivo_json='biblioteca.json'):
        self.archivo_json = archivo_json
        self.libros = self.cargar_libros()
        self.usuarios = {}  # user_id -> Usuario
        self.user_ids = set()  # Conjunto para IDs únicos

    def cargar_libros(self):
        try:
            with open(self.archivo_json, 'r') as archivo:
                datos_libros = json.load(archivo)
                return {isbn: Libro(**datos) for isbn, datos in datos_libros.items()}
        except FileNotFoundError:
            return {}

    def guardar_libros(self):
        with open(self.archivo_json, 'w') as archivo:
            json.dump({isbn: libro.to_dict() for isbn, libro in self.libros.items()}, archivo, indent=4)

    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro
        self.guardar_libros()
        print(f'Libro añadido: {libro}')

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            self.guardar_libros()
            print(f'Libro con ISBN {isbn} eliminado.')
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, usuario):
        if usuario.user_id in self.user_ids:
            print("ID de usuario ya registrado.")
        else:
            self.usuarios[usuario.user_id] = usuario
            self.user_ids.add(usuario.user_id)
            print(f'Usuario registrado: {usuario}')

    def dar_baja_usuario(self, user_id):
        if user_id in self.usuarios:
            del self.usuarios[user_id]
            self.user_ids.discard(user_id)
            print(f'Usuario con ID {user_id} dado de baja.')
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, isbn, user_id):
        libro = self.libros.get(isbn)
        usuario = self.usuarios.get(user_id)
        if libro and usuario and not libro.prestado:
            libro.prestado = True
            usuario.libros_prestados.append(isbn)
            self.guardar_libros()
            print(f"Libro '{libro.info[0]}' prestado a {usuario.nombre}.")
        else:
            print("No se puede realizar el préstamo.")

    def devolver_libro(self, isbn, user_id):
        libro = self.libros.get(isbn)
        usuario = self.usuarios.get(user_id)
        if libro and usuario and isbn in usuario.libros_prestados:
            libro.prestado = False
            usuario.libros_prestados.remove(isbn)
            self.guardar_libros()
            print(f"Libro '{libro.info[0]}' devuelto por {usuario.nombre}.")
        else:
            print("Error al devolver el libro.")

    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if criterio == "titulo" and valor.lower() in libro.info[0].lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.info[1].lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    def mostrar_libros(self):
        for libro in self.libros.values():
            print(libro)

    def listar_libros_usuario(self, user_id):
        usuario = self.usuarios.get(user_id)
        if usuario:
            print(f"Libros prestados a {usuario.nombre}:")
            for isbn in usuario.libros_prestados:
                print(self.libros[isbn])
        else:
            print("Usuario no encontrado.")

# Menú de funcionalidades
def menu():
    biblioteca = Biblioteca()
    while True:
        print("\n--- Sistema de Gestión de Biblioteca Digital ---")
        print("1. Añadir libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro")
        print("8. Mostrar libros")
        print("9. Listar libros prestados a usuario")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            biblioteca.añadir_libro(Libro(titulo, autor, categoria, isbn))
        elif opcion == '2':
            isbn = input("ISBN del libro a quitar: ")
            biblioteca.quitar_libro(isbn)
        elif opcion == '3':
            nombre = input("Nombre del usuario: ")
            user_id = input("ID de usuario: ")
            biblioteca.registrar_usuario(Usuario(nombre, user_id))
        elif opcion == '4':
            user_id = input("ID de usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(user_id)
        elif opcion == '5':
            isbn = input("ISBN del libro: ")
            user_id = input("ID del usuario: ")
            biblioteca.prestar_libro(isbn, user_id)
        elif opcion == '6':
            isbn = input("ISBN del libro: ")
            user_id = input("ID del usuario: ")
            biblioteca.devolver_libro(isbn, user_id)
        elif opcion == '7':
            criterio = input("Buscar por (titulo, autor, categoria): ").lower()
            valor = input(f"Ingrese el {criterio}: ")
            resultados = biblioteca.buscar_libros(criterio, valor)
            for libro in resultados:
                print(libro)
        elif opcion == '8':
            biblioteca.mostrar_libros()
        elif opcion == '9':
            user_id = input("ID del usuario: ")
            biblioteca.listar_libros_usuario(user_id)
        elif opcion == '0':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    menu()
