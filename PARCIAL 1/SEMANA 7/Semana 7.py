class Dispositivo:
    def __init__(self, nombre, marca, precio):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        print(f"Dispositivo '{self.nombre}' de la marca '{self.marca}' creado.")

    def mostrarInfo(self):
        print(f"Nombre: {self.nombre}")
        print(f"Marca: {self.marca}")
        print(f"Precio: ${self.precio}")

    def __del__(self):
        print(f"El dispositivo '{self.nombre}' ha sido eliminado de la memoria.")


class Smartphone(Dispositivo):
    def __init__(self, nombre, marca, precio, sistema_operativo):
        super().__init__(nombre, marca, precio)
        self.sistema_operativo = sistema_operativo
        print(f"Smartphone '{self.nombre}' con sistema operativo '{self.sistema_operativo}' creado.")

    def mostrarInfo(self):
        super().mostrarInfo()
        print(f"Sistema Operativo: {self.sistema_operativo}")

    def __del__(self):
        print(f"El smartphone '{self.nombre}' ha sido eliminado de la memoria.")


# Ejemplo de uso
dispositivo1 = Dispositivo("Laptop", "DEll", 1000)
dispositivo1.mostrarInfo()

smartphone1 = Smartphone("Galaxy S21", "Samsung", 800, "Android")
smartphone1.mostrarInfo()

# Al finalizar el script o cuando se elimina manualmente, se ejecuta el destructor
del dispositivo1
del smartphone1
