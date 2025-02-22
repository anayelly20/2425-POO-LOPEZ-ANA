class Producto:
    def __init__(self, id, nombre, cantidad, unidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.unidad = unidad
        self.precio = precio  # Precio en formato float

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad} {self.unidad}, Precio: ${self.precio:.2f}"

    def to_line(self):
        """Convierte el producto a una línea de texto para guardarlo en el archivo."""
        return f"{self.id},{self.nombre},{self.cantidad},{self.unidad},${self.precio:.2f}\n"

    @staticmethod
    def from_line(line):
        """Convierte una línea del archivo en un objeto Producto."""
        try:
            id, nombre, cantidad, unidad, precio = line.strip().split(",")
            precio = float(precio.replace("$", ""))  # Remueve el signo de dólar antes de convertirlo a float
            return Producto(id, nombre, int(cantidad), unidad, precio)
        except ValueError:
            return None  # Retorna None si hay un error en la conversión


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo al iniciar el programa."""
        productos = {}
        try:
            with open(self.archivo, "r") as f:
                for line in f:
                    producto = Producto.from_line(line)
                    if producto:
                        productos[producto.id] = producto
        except FileNotFoundError:
            print("El archivo de inventario no existe. Se creará uno nuevo.")
        except PermissionError:
            print("Error: No tienes permisos para acceder al archivo de inventario.")
        return productos

    def guardar_inventario(self):
        """Guarda todos los productos en el archivo de texto."""
        try:
            with open(self.archivo, "w") as f:
                for producto in self.productos.values():
                    f.write(producto.to_line())
        except PermissionError:
            print("Error: No se pudo guardar el inventario. Revisa los permisos del archivo.")

    def añadir_producto(self, id, nombre, cantidad, unidad, precio):
        if id in self.productos:
            print("Error: El ID ya existe.")
            return
        self.productos[id] = Producto(id, nombre, cantidad, unidad, precio)
        self.guardar_inventario()
        print(f"Producto '{nombre}' añadido con éxito.")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            self.guardar_inventario()
            print(f"Producto con ID {id} eliminado con éxito.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, unidad=None, precio=None):
        if id in self.productos:
            producto = self.productos[id]
            if cantidad is not None:
                producto.cantidad = cantidad
            if unidad is not None:
                producto.unidad = unidad
            if precio is not None:
                producto.precio = precio
            self.guardar_inventario()
            print(f"Producto con ID {id} actualizado con éxito.")
        else:
            print("Error: Producto no encontrado.")

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\nLista de productos en inventario:")
            for producto in self.productos.values():
                print(producto)


def main():
    inventario = Inventario()

    while True:
        print("\n1. Añadir producto\n2. Eliminar producto\n3. Actualizar producto\n4. Mostrar productos\n5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio por unidad de medida: ").replace("$", ""))
                unidad = input("Unidad de medida (libra, quintal, unidad, etc.): ")
                inventario.añadir_producto(id, nombre, cantidad, unidad, precio)
            except ValueError:
                print("Error: La cantidad y el precio deben ser valores numéricos.")

        elif opcion == "2":
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            unidad = input("Nueva unidad de medida (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio por unidad de medida (dejar vacío para no cambiar): ")

            cantidad = int(cantidad) if cantidad.strip() else None
            unidad = unidad.strip() if unidad.strip() else None
            precio = float(precio.replace("$", "")) if precio.strip() else None

            inventario.actualizar_producto(id, cantidad, unidad, precio)

        elif opcion == "4":
            inventario.mostrar_productos()

        elif opcion == "5":
            print("Saliendo...")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
