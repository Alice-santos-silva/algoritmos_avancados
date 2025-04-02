class GrafoLista:
    def __init__(self):
        self.lista_adjacencia = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2, peso):
        if vertice1 in self.lista_adjacencia and vertice2 in self.lista_adjacencia:
            self.lista_adjacencia[vertice1].append((vertice2, peso))
            self.lista_adjacencia[vertice2].append((vertice1, peso))

    def mostrar_grafo(self):
        for vertice in self.lista_adjacencia:
            conexoes = [f"{v}({p}km)" for v, p in self.lista_adjacencia[vertice]]
            print(f"{vertice} -> {conexoes}")

    def mostrar_vizinhos(self, vertice):
        if vertice in self.lista_adjacencia:
            conexoes = [f"{v}({p}km)" for v, p in self.lista_adjacencia[vertice]]
            print(f"Vizinhos de {vertice}: {conexoes}")
        else:
            print(f"O vértice {vertice} não existe no grafo.")


class GrafoMatriz:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matriz = [[0] * num_vertices for _ in range(num_vertices)]
        self.vertices = {}
        self.indice_para_vertice = {}
        self.contador = 0

    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices and self.contador < self.num_vertices:
            self.vertices[vertice] = self.contador
            self.indice_para_vertice[self.contador] = vertice
            self.contador += 1

    def adicionar_aresta(self, vertice1, vertice2, peso):
        if vertice1 in self.vertices and vertice2 in self.vertices:
            i, j = self.vertices[vertice1], self.vertices[vertice2]
            self.matriz[i][j] = peso
            self.matriz[j][i] = peso

    def mostrar_matriz(self):
        print("Matriz de Adjacência:")
        print("    ", end="")
        for v in self.vertices.keys():
            print(f"{v:4}", end="")
        print()
        
        for i in range(self.num_vertices):
            if i in self.indice_para_vertice:
                print(f"{self.indice_para_vertice[i]}  ", end="")
                for j in range(self.num_vertices):
                    print(f"{self.matriz[i][j]:4}", end="")
                print()

    def mostrar_vizinhos(self, vertice):
        if vertice in self.vertices:
            indice = self.vertices[vertice]
            vizinhos = [f"{self.indice_para_vertice[i]}({self.matriz[indice][i]}km)" 
                        for i in range(self.num_vertices) 
                        if self.matriz[indice][i] > 0]
            print(f"Vizinhos de {vertice}: {vizinhos}")
        else:
            print(f"O vértice {vertice} não existe no grafo.")


grafo_lista = GrafoLista()

for bairro in ["A", "B", "C", "D", "E", "F"]:
    grafo_lista.adicionar_vertice(bairro)

conexoes = [
    ("A", "B", 4), ("A", "C", 2),
    ("B", "C", 5), ("B", "D", 5),
    ("C", "D", 8), ("C", "E", 3),
    ("D", "F", 6),
    ("E", "F", 1)
]

for origem, destino, peso in conexoes:
    grafo_lista.adicionar_aresta(origem, destino, peso)

print("Lista de Adjacência do Grafo:")
grafo_lista.mostrar_grafo()

grafo_matriz = GrafoMatriz(6)

for bairro in ["A", "B", "C", "D", "E", "F"]:
    grafo_matriz.adicionar_vertice(bairro)

for origem, destino, peso in conexoes:
    grafo_matriz.adicionar_aresta(origem, destino, peso)

grafo_matriz.mostrar_matriz()