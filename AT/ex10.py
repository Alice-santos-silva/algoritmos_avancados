class Grafo:
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
            conexoes = [f"{v}(peso:{p})" for v, p in self.lista_adjacencia[vertice]]
            print(f"{vertice} -> {conexoes}")

    def mostrar_vizinhos(self, vertice):
        if vertice in self.lista_adjacencia:
            conexoes = [f"{v}(peso:{p})" for v, p in self.lista_adjacencia[vertice]]
            print(f"Vizinhos de {vertice}: {conexoes}")
        else:
            print(f"O vértice {vertice} não existe no grafo.")
    
    def prim(self):
        if not self.lista_adjacencia:
            return [], 0
        
        inicio = next(iter(self.lista_adjacencia))
        incluidos = {inicio}
        mst = []
        custo_total = 0
        
        while len(incluidos) < len(self.lista_adjacencia):
            menor_peso = float('inf')
            aresta_escolhida = None
            
            for vertice in incluidos:
                for vizinho, peso in self.lista_adjacencia[vertice]:
                    if vizinho not in incluidos and peso < menor_peso:
                        menor_peso = peso
                        aresta_escolhida = (vertice, vizinho, peso)
            
            if aresta_escolhida is None:
                break
            
            v1, v2, peso = aresta_escolhida
            incluidos.add(v2)
            mst.append(aresta_escolhida)
            custo_total += peso
        
        return mst, custo_total

if __name__ == "__main__":
    grafo = Grafo()
    
    vertices = ["A", "B", "C", "D", "E", "F", "G"]
    for v in vertices:
        grafo.adicionar_vertice(v)
    
    arestas = [
        ("A", "B", 7), ("A", "D", 5),
        ("B", "C", 8), ("B", "D", 9), ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15), ("D", "F", 6),
        ("E", "F", 8), ("E", "G", 9),
        ("F", "G", 11)
    ]
    
    for v1, v2, peso in arestas:
        grafo.adicionar_aresta(v1, v2, peso)
    
    print("Lista de Adjacência do Grafo:")
    grafo.mostrar_grafo()
    
    mst, custo_total = grafo.prim()
    
    print("\nÁrvore Geradora Mínima (MST):")
    for v1, v2, peso in mst:
        print(f"{v1} -- {v2} : {peso}")
    
    print(f"\nCusto total da MST: {custo_total}")