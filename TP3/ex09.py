class GrafoAlgoritmoPrim:
    def __init__(self, cidades):
        self.V = cidades  
        self.grafo = [[0] * cidades for _ in range(cidades)]  

    def adicionar_aresta(self, u, v, custo):
        self.grafo[u][v] = custo
        self.grafo[v][u] = custo  

    def prim(self):
        infinito = float('inf')
        selecionado = [False] * self.V  
        chave = [infinito] * self.V  
        pai = [-1] * self.V  

        chave[0] = 0  

        for _ in range(self.V):
            minimo = infinito
            u = -1
            for v in range(self.V):
                if not selecionado[v] and chave[v] < minimo:
                    minimo = chave[v]
                    u = v

            selecionado[u] = True  

            for v in range(self.V):
                if 0 < self.grafo[u][v] < chave[v] and not selecionado[v]:
                    chave[v] = self.grafo[u][v]
                    pai[v] = u

        print("\nConjunto de conexões mais econômico:")
        custo_total = 0
        for i in range(1, self.V):
            print(f"{pai[i]} - {i} (Custo: {self.grafo[i][pai[i]]})")
            custo_total += self.grafo[i][pai[i]]
        print(f"Total: {custo_total}")

g = GrafoAlgoritmoPrim(6)

conexoes = [
    (0, 1, 4), (0, 2, 2), (1, 2, 5),
    (1, 3, 10), (2, 3, 8), (2, 4, 3),
    (3, 4, 7), (3, 5, 6), (4, 5, 1)
]

for u, v, custo in conexoes:
    g.adicionar_aresta(u, v, custo)

g.prim()
