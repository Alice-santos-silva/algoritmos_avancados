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

    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 in self.vertices and vertice2 in self.vertices:
            i, j = self.vertices[vertice1], self.vertices[vertice2]
            self.matriz[i][j] = 1
            self.matriz[j][i] = 1  


    def mostrar_matriz(self):
        print("Matriz de Adjacência:")
        print("  ", "  ".join(self.vertices.keys()))  
        for i, linha in enumerate(self.matriz):
            print(self.indice_para_vertice[i], linha)

    def mostrar_vizinhos(self, vertice):
        if vertice in self.vertices:
            indice = self.vertices[vertice]
            vizinhos = [self.indice_para_vertice[i] for i in range(self.num_vertices) if self.matriz[indice][i] == 1]
            print(f"Vizinhos de {vertice}: {vizinhos}")
        else:
            print(f"O vértice {vertice} não existe no grafo.")


grafo = GrafoMatriz(4)

for v in ["A", "B", "C", "D"]:
    grafo.adicionar_vertice(v)

arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")]
for v1, v2 in arestas:
    grafo.adicionar_aresta(v1, v2)

grafo.mostrar_matriz()

