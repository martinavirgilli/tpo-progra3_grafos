# Biblioteca heapq para manejar la cola de prioridad
import heapq


class Grafo:
    def __init__(self):
        # Inicializar grafo con vértices y aristas
        self.grafo = {
            "A": [("B", 1), ("C", 2)],
            "B": [("A", 1), ("D", 3), ("E", 4)],
            "C": [("A", 2), ("F", 5)],
            "D": [("B", 3), ("G", 6)],
            "E": [("B", 4), ("H", 7)],
            "F": [("C", 5), ("G", 8)],
            "G": [("D", 6), ("F", 8), ("H", 9)],
            "H": [("E", 7), ("G", 9)]
        }

    # Obtener todos los vértices del grafo
    def obtener_vertices(self):
        return list(self.grafo.keys())

    # Obtener todas las aristas de un vértice
    def obtener_aristas(self, vertice):
        return self.grafo[vertice]

    # Mostrar el grafo en la consola
    def mostrar_grafo(self):
        for vertice, aristas in self.grafo.items():
            print(f"Vértice {vertice} está conectado a: {aristas}")


class Prim:
    def __init__(self, grafo):
        # Inicializar clase grafo
        self.grafo = grafo

    # Aplicar el algoritmo de Prim
    def aplicar(self):
        # Inicializar árbol de expansión mínima y conjunto de vértices usados
        aem = []
        usados = set([self.grafo.obtener_vertices()[0]])

        # Crear lista de todas las aristas válidas y convertirlas en cola prioridad
        aristas_validas = [
            (costo, vertice, adyacente)
            for vertice, adyacentes in self.grafo.grafo.items()
            for adyacente, costo in adyacentes
        ]
        heapq.heapify(aristas_validas)

        # Mientras haya aristas válidas
        while aristas_validas:
            # Obtener la arista con menor costo
            costo, vertice, adyacente = heapq.heappop(aristas_validas)

            # Si el vértice adyacente no se usó
            if adyacente not in usados:
                # Se añade al conjunto de vértices usados y a la lista AEM
                usados.add(adyacente)
                aem.append((vertice, adyacente, costo))

                # Añadir las aristas adyacentes al vértice adyacente a la cola prioridad
                for siguiente, costo in self.grafo.grafo[adyacente]:
                    if siguiente not in usados:
                        heapq.heappush(aristas_validas, (costo, adyacente, siguiente))

        return aem
    

class Floyd:
    def __init__(self, grafo):
        # Inicializar clase grafo
        self.grafo = grafo.grafo
        self.vertices = grafo.obtener_vertices()

    def aplicar(self):
        # Inicializar matriz de distancias con valores infinitos
        distancias = {v: {w: float('inf') for w in self.vertices} for v in self.vertices}
        for v in self.vertices:
            distancias[v][v] = 0
        for v, aristas in self.grafo.items():
            for w, peso in aristas:
                distancias[v][w] = peso

        for k in self.vertices:
            for v in self.vertices:
                for w in self.vertices:
                    distancias[v][w] = min(distancias[v][w], distancias[v][k] + distancias[k][w])

        return distancias
    


if __name__ == "__main__":
    g = Grafo()
    g.mostrar_grafo()
    print()
    f = Floyd(g)

    p = Prim(g)
    arbol_expansion_minima = p.aplicar()
    print("Arbol de expansión mínima Prim: ", arbol_expansion_minima)
    print()

    distancias = f.aplicar()
    print("Distancia entre pares (Floyd)", distancias)