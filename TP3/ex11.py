class RedeTelefonia:
    def __init__(self, regioes):
        self.R = regioes  
        self.mapa = [[0] * regioes for _ in range(regioes)]  

    def adicionar_conexao(self, r1, r2, custo):
        self.mapa[r1][r2] = custo
        self.mapa[r2][r1] = custo 

    def calcular_agm(self):
        infinito = float('inf')
        conectadas = [False] * self.R 
        menor_custo = [infinito] * self.R  
        origem = [-1] * self.R 

        menor_custo[0] = 0  

        for _ in range(self.R):
            min_custo = infinito
            regiao = -1
            for r in range(self.R):
                if not conectadas[r] and menor_custo[r] < min_custo:
                    min_custo = menor_custo[r]
                    regiao = r

            conectadas[regiao] = True  

            for r in range(self.R):
                if 0 < self.mapa[regiao][r] < menor_custo[r] and not conectadas[r]:
                    menor_custo[r] = self.mapa[regiao][r]
                    origem[r] = regiao

        print("\nConjunto mínimo de conexões necessárias para cobrir todas as regiões.")
        custo_total = 0
        for i in range(1, self.R):
            print(f"Região {origem[i]} - Região {i} (Custo: {self.mapa[i][origem[i]]})")
            custo_total += self.mapa[i][origem[i]]
        print(f"Custo total da infraestrutura: {custo_total}")

rede = RedeTelefonia(6)

conexoes = [
    (0, 1, 4), (0, 2, 2), (1, 2, 5),
    (1, 3, 10), (2, 3, 8), (2, 4, 3),
    (3, 4, 7), (3, 5, 6), (4, 5, 1)
]

for r1, r2, custo in conexoes:
    rede.adicionar_conexao(r1, r2, custo)

rede.calcular_agm()
