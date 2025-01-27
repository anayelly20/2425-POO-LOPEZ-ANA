# Calcula el área de un círculo dado su radio
# El programa también verifica si el área es mayor que un valor específico

import math

# Función que calcula el área de un círculo

def calcular_area_circulo(radio):
    # El área de un círculo se calcula con la fórmula A = pi * radio^2
    area = math.pi * radio ** 2
    return area

# Función que verifica si el área es mayor a un valor dado
def es_area_mayor_que(area, valor_comparacion):
    # Retorna True si el área es mayor que el valor de comparación, False en caso contrario
    return area > valor_comparacion

# Datos de entrada (radio del círculo y valor de comparación)
radio_circulo = 5  # radio del círculo (tipo de dato integer)
valor_comparacion = 50.0  # valor para comparar el área (tipo de dato float)

# Calculamos el área del círculo
area_del_circulo = calcular_area_circulo(radio_circulo)

# Imprimimos el resultado en un mensaje descriptivo
print(f"El área del círculo con radio {radio_circulo} es: {area_del_circulo:.2f}")

# Verificamos si el área es mayor que el valor de comparación
es_mayor = es_area_mayor_que(area_del_circulo, valor_comparacion)

# Mostramos el resultado de la comparación
if es_mayor:
    print(f"El área del círculo es mayor que {valor_comparacion}.")
else:
    print(f"El área del círculo no es mayor que {valor_comparacion}.")
