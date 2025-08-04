class SimulacionClientes:
    def __init__(self, capacidad):
        self.cola = []
        self.capacidad = capacidad

    def is_empty(self):
        return len(self.cola) == 0

    def is_full(self):
        return len(self.cola) == self.capacidad

    def addCustomer(self, nombre):
        if self.is_full():
            print(f"La cola está llena. No se puede agregar a {nombre}")
        else:
            self.cola.append(nombre)
            print(f"Cliente agregado: {nombre}")

    def serveCustomer(self):
        if self.is_empty():
            print("No hay clientes para atender.")
        else:
            cliente = self.cola.pop(0)
            print(f"Atendiendo a: {cliente}")

# Se crea la cola con capacidad de 3
cola = SimulacionClientes(capacidad=3)

cola.addCustomer("Esteban")
cola.addCustomer("Sebastian")
cola.addCustomer("Jose")


cola.addCustomer("Felipe") # -> debe fallar


cola.serveCustomer()  # Primero: Juan
cola.serveCustomer()  # Segundo: María


cola.addCustomer("Felipe")  # -> Ahora sí entra

# Se atienden los restantes
cola.serveCustomer()  # Pedro
cola.serveCustomer()  # Lucía

# Cola vacía: intentar atender otro
cola.serveCustomer()  # No hay clientes

