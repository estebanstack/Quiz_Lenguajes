class RecomendadorProductos:
    def __init__(self):
        self.compras = {}  # usuario -> set(productos)

    def addPurchase(self, usuario, producto):
        if usuario not in self.compras:
            self.compras[usuario] = set()
        self.compras[usuario].add(producto)

    def getRecommendations(self, usuario):
        if usuario not in self.compras:
            return []

        productos_usuario = self.compras[usuario]
        recomendaciones = {}

        # Buscar usuarios similares
        for otro_usuario, productos in self.compras.items():
            if otro_usuario == usuario:
                continue
            interseccion = productos & productos_usuario
            if interseccion:
                for producto in productos:
                    if producto not in productos_usuario:
                        if producto not in recomendaciones:
                            recomendaciones[producto] = 0
                        recomendaciones[producto] += 1

        # Ordenar por mayor frecuencia
        recomendaciones_ordenadas = sorted(recomendaciones.items(), key=lambda x: -x[1])
        return [prod for prod, _ in recomendaciones_ordenadas]

r = RecomendadorProductos()

# Compras de varios usuarios
r.addPurchase("Esteban", "Laptop")
r.addPurchase("Esteban", "Teclado")

r.addPurchase("María", "Laptop")
r.addPurchase("María", "Mouse")

r.addPurchase("Juan", "Laptop")
r.addPurchase("Juan", "Audífonos")

r.addPurchase("Olga", "Mouse")
r.addPurchase("Olga", "Alfombrilla")

# Recomendaciones para Esteban
print("Recomendaciones para Esteban:", r.getRecommendations("Esteban"))

