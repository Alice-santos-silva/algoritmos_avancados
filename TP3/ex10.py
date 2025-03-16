class GrafoAlgoritmoPrim:
    def __init__(self, bairros):
        self.V = bairros  
        self.grafo = [[0] * bairros for _ in range(bairros)]  

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

        print("\nMelhor plano de instalação:")
        custo_total = 0
        for i in range(1, self.V):
            print(f"{bairros[i]} <-> {bairros[pai[i]]} (Custo: {self.grafo[i][pai[i]]})")
            custo_total += self.grafo[i][pai[i]]
        print(f"Custo total do plano: {custo_total}")


bairros = ["Copacabana", "Ipanema", "Leblon", "Botafogo", "Flamengo", "Lapa"]

g = GrafoAlgoritmoPrim(len(bairros))

tubulacoes = [
    (0, 1, 10), (0, 2, 12), (1, 2, 8),
    (1, 3, 15), (2, 3, 7), (2, 4, 6),
    (3, 4, 11), (3, 5, 14), (4, 5, 9)
]

for u, v, custo in tubulacoes:
    g.adicionar_aresta(u, v, custo)

g.prim()
