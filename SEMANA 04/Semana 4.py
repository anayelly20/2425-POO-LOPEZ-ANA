class Moto:
    def __init__(self, modelo, anio):
        self.modelo = modelo
        self.anio = anio
        self.conductor = None  # Inicialmente, la moto no tiene conductor

    def asignar_conductor(self, persona):
        if isinstance(persona, Persona):
            self.conductor = persona
        else:
            print("Error: Solo se pueden asignar objetos de tipo Persona como conductor.")

    def __str__(self):
        return f'Moto {self.modelo} del año {self.anio}, conducida por {self.conductor.nombre if self.conductor else "nadie"}.'


class Persona:
    def __init__(self, nombre, licencia):
        self.nombre = nombre
        self.licencia = licencia

    def __str__(self):
        return f'Persona {self.nombre} con licencia número {self.licencia}.'


class SistemaDeGestion:
    def __init__(self):
        self.motos = []
        self.personas = []

    def agregar_moto(self, modelo, anio):
        nueva_moto = Moto(modelo, anio)
        self.motos.append(nueva_moto)
        print(f'Moto {modelo} del año {anio} agregada al sistema.')

    def agregar_persona(self, nombre, licencia):
        nueva_persona = Persona(nombre, licencia)
        self.personas.append(nueva_persona)
        print(f'Persona {nombre} con licencia número {licencia} agregada al sistema.')

    def asignar_conductor_a_moto(self, moto_indice, persona_indice):
        if moto_indice < len(self.motos) and persona_indice < len(self.personas):
            self.motos[moto_indice].asignar_conductor(self.personas[persona_indice])
            print(f'Conductor {self.personas[persona_indice].nombre} asignado a la moto {self.motos[moto_indice].modelo}.')
        else:
            print("Error: Índice de moto o persona inválido.")

    def mostrar_estado(self):
        print("\nEstado del sistema:")
        for moto in self.motos:
            print(moto)
        for persona in self.personas:
            print(persona)


# Ejemplo de uso
sistema = SistemaDeGestion()

# Agregar motos
sistema.agregar_moto('Sheneray', 2019)
sistema.agregar_moto('Deportiva', 2024)

# Agregar personas
sistema.agregar_persona('Giss', 2)
sistema.agregar_persona('Dilan', 4)

# Asignar conductores
sistema.asignar_conductor_a_moto(0, 0)  # Laura a la Yamaha
sistema.asignar_conductor_a_moto(1, 1)  # Carlos a la Ducati

# Mostrar estado
sistema.mostrar_estado()
