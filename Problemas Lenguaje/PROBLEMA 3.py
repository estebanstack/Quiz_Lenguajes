class Arbol:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class AutocompletarArbol:
    def __init__(self):
        self.root = Arbol()

    def insert(self, word):
        nodo = self.root
        for letra in word:
            if letra not in nodo.children:
                nodo.children[letra] = Arbol()
            nodo = nodo.children[letra]
        nodo.is_end_of_word = True

    def buscar_palabras(self, nodo, prefix, resultados):
        if nodo.is_end_of_word:
            resultados.append(prefix)
        for letra, child in nodo.children.items():
            self.buscar_palabras(child, prefix + letra, resultados)

    def autocomplete(self, prefix):
        nodo = self.root
        for letra in prefix:
            if letra not in nodo.children:
                return []  # No hay coincidencias
            nodo = nodo.children[letra]
        resultados = []
        self.buscar_palabras(nodo, prefix, resultados)
        return resultados
    

trie = AutocompletarArbol()
palabras = ["carro", "cat", "carta", "carbon", "dog", "door", "dove"]
for palabra in palabras:
    trie.insert(palabra)

# Pruebas de autocompletar
print(trie.autocomplete("ca"))   # ['carro', 'carta', 'carbon', 'cat']
print(trie.autocomplete("car"))  # ['carro', 'carta', 'carbon']
print(trie.autocomplete("do"))   # ['dog', 'door', 'dove']
print(trie.autocomplete("z"))    # []
print(trie.autocomplete(""))     # Todas las palabras



