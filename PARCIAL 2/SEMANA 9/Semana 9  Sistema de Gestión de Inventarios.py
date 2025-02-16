class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id, self.nombre, self.cantidad, self.precio = id_producto, nombre, cantidad, precio

    def actualizar(self, cantidad=None, precio=None):
        if cantidad: self.cantidad = cantidad
        if precio: self.precio = precio

    def __str__(self):
        return f"ID: {self.id} | {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        if any(p.id == producto.id for p in self.productos):
            print("Error: ID duplicado.")
        else:
            self.productos.append(producto)
            print("Producto agregado.")

    def eliminar(self, id_producto):
        self.productos = [p for p in self.productos if p.id != id_producto]
        print("Producto eliminado.")

    def actualizar(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.id == id_producto:
                p.actualizar(cantidad, precio)
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

    def buscar(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        print(*encontrados if encontrados else ["No encontrado"], sep="\n")

    def mostrar(self):
        print(*self.productos if self.productos else ["Inventario vacío"], sep="\n")


def menu():
    inventario = Inventario()
    opciones = {
        '1': lambda: inventario.agregar(
            Producto(input("ID: "), input("Nombre: "), int(input("Cantidad: ")), float(input("Precio: ")))),
        '2': lambda: inventario.eliminar(input("ID: ")),
        '3': lambda: inventario.actualizar(input("ID: "),
                                           cantidad=int(input("Cantidad: ")) if (c := input("Cantidad: ")) else None,
                                           precio=float(input("Precio: ")) if (p := input("Precio: ")) else None),
        '4': lambda: inventario.buscar(input("Nombre: ")),
        '5': inventario.mostrar,
        '6': exit
    }
    while True:
        print("\n1. Agregar\n2. Eliminar\n3. Actualizar\n4. Buscar\n5. Mostrar\n6. Salir")
        opciones.get(input("Opción: "), lambda: print("Opción inválida"))()


if __name__ == "__main__":
    menu()


