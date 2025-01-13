#     Tarea Nomenclatura en Python

# Clases: CamelCase (cada palabra comienza con mayúscula)
class MotoElectrica:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_informacion(self):
        return f"Moto Eléctrica: {self.marca} {self.modelo}"

# Funciones y variables: snake_case (palabras separadas por guiones bajos)
def calcular_distancia(rendimiento, energia):
    return rendimiento * energia

# Constantes: MAYUSCULAS con guiones bajos
MAX_ENERGIA = 70  # Capacidad máxima de energía de la moto en kWh

# Instancia de la clase
mi_moto = MotoElectrica("Sheneray", "Lifan's")

# Llamada a función
rendimiento = 2.4  # Km por kWh
distancia = calcular_distancia(rendimiento, MAX_ENERGIA)

print(mi_moto.mostrar_informacion())
print(f"Distancia máxima posible: {distancia} km")
