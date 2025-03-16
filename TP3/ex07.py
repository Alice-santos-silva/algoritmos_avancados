class GrafoFibraOptica:
    def __init__(self, bairros):
        self.V = bairros  
        self.grafo = [[0] * bairros for _ in range(bairros)]  

    def adicionar_conexao(self, u, v, custo):
        self.grafo[u][v] = custo
        self.grafo[v][u] = custo  

    def prim(self):
        infinito = float('inf')
        selecionado = [False] * self.V  
        custo_conexao = [infinito] * self.V  
        pai = [-1] * self.V  

        custo_conexao[0] = 0  

        for _ in range(self.V):
            minimo = infinito
            u = -1
            for v in range(self.V):
                if not selecionado[v] and custo_conexao[v] < minimo:
                    minimo = custo_conexao[v]
                    u = v

            selecionado[u] = True 

            for v in range(self.V):
                if 0 < self.grafo[u][v] < custo_conexao[v] and not selecionado[v]:
                    custo_conexao[v] = self.grafo[u][v]
                    pai[v] = u

        custo_total = 0
        for i in range(1, self.V):
            print(f"Bairro {pai[i]} - Bairro {i} (Custo: {self.grafo[i][pai[i]]})")
            custo_total += self.grafo[i][pai[i]]
        print(f"Custo total da instalação: {custo_total}")

g = GrafoFibraOptica(6)

conexoes = [
    (0, 1, 4), (0, 2, 2), (1, 2, 5),
    (1, 3, 10), (2, 3, 8), (2, 4, 3),
    (3, 4, 7), (3, 5, 6), (4, 5, 1)
]

for u, v, custo in conexoes:
    g.adicionar_conexao(u, v, custo)

g.prim()
