class Dispositivo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Computadora(Dispositivo):  # Herencia de la clase Dispositivo
    def __init__(self, marca, modelo, memoria_ram):
        super().__init__(marca, modelo)  # Llamada al constructor de la clase base
        self.memoria_ram = memoria_ram

    # Método específico de la clase Computadora
    def mostrar_informacion(self):
        return f"Computadora {self.marca} {self.modelo}, con {self.memoria_ram}GB de RAM"

class Smartphone(Dispositivo):
    def __init__(self, marca, modelo, capacidad_bateria):
        super().__init__(marca, modelo)
        self.capacidad_bateria = capacidad_bateria

    def mostrar_informacion(self):
        return f"Smartphone {self.marca} {self.modelo}, con {self.capacidad_bateria}mAh de batería"

# Creación de un objeto de la clase Computadora
mi_computadora = Computadora("Lenovo", "ThinkPad X1", 16)
print(mi_computadora.mostrar_informacion())

# Creación de un objeto de la clase Smartphone
mi_smartphone = Smartphone("Samsung", "Galaxy S23", 5000)
print(mi_smartphone.mostrar_informacion())
