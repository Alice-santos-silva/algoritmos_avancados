import heapq

class Mapa:
    def __init__(self):
        self.adj = {}
    
    def adicionar_vertice(self, vertice):
        if vertice not in self.adj:
            self.adj[vertice] = {}
    
    def adicionar_aresta(self, v1, v2, peso):
        if v1 in self.adj and v2 in self.adj:
            self.adj[v1][v2] = peso
            self.adj[v2][v1] = peso
    
    def dijkstra(self, origem, destino):
        fila = [(0, origem, [])]
        visitados = set()
        
        while fila:
            dist, atual, caminho = heapq.heappop(fila)
            
            if atual in visitados:
                continue
            
            caminho = caminho + [atual]
            visitados.add(atual)
            
            if atual == destino:
                return caminho, dist
            
            for vizinho, peso in self.adj[atual].items():
                if vizinho not in visitados:
                    heapq.heappush(fila, (dist + peso, vizinho, caminho))
        
        return None, float('inf')

mapa = Mapa()
vertices = ["CD", "A", "B", "C", "D", "E", "F"]
for v in vertices:
    mapa.adicionar_vertice(v)

arestas = [
    ("CD", "A", 4), ("CD", "B", 2), ("A", "C", 5), ("A", "D", 10),
    ("B", "A", 3), ("B", "D", 8), ("C", "D", 2), ("C", "E", 4),
    ("D", "E", 6), ("D", "F", 5), ("E", "F", 3)
]
for v1, v2, peso in arestas:
    mapa.adicionar_aresta(v1, v2, peso)

rota, distancia = mapa.dijkstra("CD", "F")
print(f"Rota ótima: {' -> '.join(rota)}")
print(f"Distância mínima: {distancia} km")
