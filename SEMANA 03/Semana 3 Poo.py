class WeatherRecord:
    def __init__(self):
        # Lista privada para almacenar temperaturas diarias
        self.__daily_temperatures = []

    def add_daily_temperature(self, temperature):
        """Agrega la temperatura diaria a la lista."""
        self.__daily_temperatures.append(temperature)

    def calculate_weekly_average(self):
        """Calcula y retorna el promedio semanal de temperaturas."""
        if not self.__daily_temperatures:
            return 0  # Evita división por cero
        return sum(self.__daily_temperatures) / len(self.__daily_temperatures)

    def get_daily_temperatures(self):
        """Retorna la lista de temperaturas diarias."""
        return self.__daily_temperatures

# Uso de la clase para gestionar datos climáticos
weather = WeatherRecord()

# Agregar temperaturas diarias
weather.add_daily_temperature(20)
weather.add_daily_temperature(22)
weather.add_daily_temperature(19)
weather.add_daily_temperature(21)
weather.add_daily_temperature(18)
weather.add_daily_temperature(23)
weather.add_daily_temperature(20)

# Calcular y mostrar el promedio semanal
average = weather.calculate_weekly_average()
print("Promedio semanal de temperatura (POO):", average)

# Mostrar temperaturas diarias
print("Temperaturas diarias registradas (POO):", weather.get_daily_temperatures())
