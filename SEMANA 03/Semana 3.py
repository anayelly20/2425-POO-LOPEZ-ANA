# Variables globales
daily_temperatures = []

# Función para agregar temperatura diaria
def add_daily_temperature(temperature):
    global daily_temperatures
    daily_temperatures.append(temperature)

# Función para calcular el promedio semanal de temperaturas
def calculate_weekly_average():
    global daily_temperatures
    if not daily_temperatures:
        return 0  # Evita división por cero
    return sum(daily_temperatures) / len(daily_temperatures)

# Registrar temperaturas diarias
add_daily_temperature(20)
add_daily_temperature(22)
add_daily_temperature(19)
add_daily_temperature(21)
add_daily_temperature(18)
add_daily_temperature(23)
add_daily_temperature(20)

# Calcular y mostrar el promedio semanal
average = calculate_weekly_average()
print("Promedio semanal de temperatura (Tradicional):", average)

# Mostrar temperaturas diarias
print("Temperaturas diarias registradas (Tradicional):", daily_temperatures)
