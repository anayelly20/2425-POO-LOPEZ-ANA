class Producto:
    def __init__(self, nombre, fecha_caducidad):
        self.nombre = nombre
        self.fecha_caducidad = fecha_caducidad
        self.comprador = None  # Inicialmente, el producto no tiene comprador

    def asignar_comprador(self, persona):
        if isinstance(persona, Persona):
            self.comprador = persona
        else:
            print("Error: Solo se pueden asignar objetos de tipo Persona como comprador.")

    def __str__(self):
        return f'Producto: {self.nombre}, fecha de caducidad: {self.fecha_caducidad}, comprado por {self.comprador.nombre if self.comprador else "nadie"}.'


class Persona:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion

    def __str__(self):
        return f'Persona: {self.nombre}, ID: {self.identificacion}.'


class TiendaDeProductos:
    def __init__(self):
        self.productos = []
        self.personas = []

    def agregar_producto(self, nombre, fecha_caducidad):
        nuevo_producto = Producto(nombre, fecha_caducidad)
        self.productos.append(nuevo_producto)
        print(f'Producto {nombre} con fecha de caducidad {fecha_caducidad} agregado a la tienda.')

    def agregar_persona(self, nombre, identificacion):
        nueva_persona = Persona(nombre, identificacion)
        self.personas.append(nueva_persona)
        print(f'Persona {nombre} con ID {identificacion} agregada al sistema.')

    def asignar_comprador_a_producto(self, producto_indice, persona_indice):
        if producto_indice < len(self.productos) and persona_indice < len(self.personas):
            self.productos[producto_indice].asignar_comprador(self.personas[persona_indice])
            print(f'Comprador {self.personas[persona_indice].nombre} asignado al producto {self.productos[producto_indice].nombre}.')
        else:
            print("Error: Índice de producto o persona inválido.")

    def mostrar_estado(self):
        print("\nEstado de la tienda:")
        for producto in self.productos:
            print(producto)
        for persona in self.personas:
            print(persona)


# Ejemplo de uso
tienda = TiendaDeProductos()

# Agregar productos
tienda.agregar_producto('Arroz', '2025-12-31')
tienda.agregar_producto('Aceite', '2024-06-30')

# Agregar personas
tienda.agregar_persona('Ana', 101)
tienda.agregar_persona('Jorge', 102)

# Asignar compradores
tienda.asignar_comprador_a_producto(0, 0)  # Ana compra el arroz
tienda.asignar_comprador_a_producto(1, 1)  # Jorge compra el aceite

# Mostrar estado
tienda.mostrar_estado()
