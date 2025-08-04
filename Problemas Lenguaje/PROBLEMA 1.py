class simulacionWeb:
    def __init__(self):
        self.pila_anteriores = []
        self.pila_posteriores = []
        self.pagina_actual = None

    def loadPage(self, url):
        if self.pagina_actual:
            self.pila_anteriores.append(self.pagina_actual)
        self.pagina_actual = url
        self.pila_posteriores.clear()  # Al cargar una nueva página, se borra el historial hacia adelante
        print(f"Cargando: {self.pagina_actual}")

    def goBack(self):
        if not self.pila_anteriores:
            print("No hay páginas anteriores.")
            return
        self.pila_posteriores.append(self.pagina_actual)
        self.pagina_actual = self.pila_anteriores.pop()
        print(f"Retrocediendo a: {self.pagina_actual}")

    def goForward(self):
        if not self.pila_posteriores:
            print("No hay páginas siguientes.")
            return
        self.pila_anteriores.append(self.pagina_actual)
        self.pagina_actual = self.pila_posteriores.pop()
        print(f"Avanzando a: {self.pagina_actual}")


nav = simulacionWeb()

nav.loadPage("usergio.com")
nav.loadPage("youtube.com")
nav.loadPage("netflix.com")

nav.goBack()     
nav.goForward()  
nav.goForward()  
nav.goForward()  
