class GrafoAeroportos:
    def __init__(self):
        self.aeroportos = {}

    def adicionar_aeroporto(self, aeroporto):
        if aeroporto not in self.aeroportos:
            self.aeroportos[aeroporto] = {}

    def adicionar_voo(self, aeroporto1, aeroporto2, custo, tempo_conexao, escala_obrigatoria=False, custo_escala=0):
        custo_total = custo + (custo_escala if escala_obrigatoria else 0)
        self.aeroportos[aeroporto1][aeroporto2] = (custo_total, tempo_conexao)
        self.aeroportos[aeroporto2][aeroporto1] = (custo_total, tempo_conexao)  

    def dijkstra(self, origem, destino, tempo_maximo):
        nao_visitados = list(self.aeroportos.keys())  
        custos = {aeroporto: float("inf") for aeroporto in self.aeroportos}  
        custos[origem] = 0  
        tempos_conexao = {aeroporto: float("inf") for aeroporto in self.aeroportos}  
        tempos_conexao[origem] = 0  
        predecessores = {}  

        while nao_visitados:
            aeroporto_atual = min(nao_visitados, key=lambda aeroporto: custos[aeroporto])

            if custos[aeroporto_atual] == float("inf"):
                break  

            for vizinho, (custo_voo, tempo) in self.aeroportos[aeroporto_atual].items():
                if tempos_conexao[aeroporto_atual] + tempo <= tempo_maximo:
                    nova_distancia = custos[aeroporto_atual] + custo_voo
                    if nova_distancia < custos[vizinho]:  
                        custos[vizinho] = nova_distancia
                        tempos_conexao[vizinho] = tempos_conexao[aeroporto_atual] + tempo
                        predecessores[vizinho] = aeroporto_atual  

            nao_visitados.remove(aeroporto_atual) 

        caminho = []
        aeroporto_atual = destino
        while aeroporto_atual in predecessores:
            caminho.append(aeroporto_atual)
            aeroporto_atual = predecessores[aeroporto_atual]
        caminho.append(origem)
        caminho.reverse()

        return caminho, custos[destino]

aeroporto_mapa = GrafoAeroportos()
aeroportos = ["A", "B", "C", "D", "E"]

for aeroporto in aeroportos:
    aeroporto_mapa.adicionar_aeroporto(aeroporto)

voos = [
    ("A", "B", 240, 2, False, 0), ("A", "C", 660, 3, True, 50),
    ("B", "C", 550, 1, False, 0), ("B", "D", 700, 4, False, 0),
    ("C", "E", 300, 2, True, 100), ("D", "E", 310, 3, False, 0),
]

for aeroporto1, aeroporto2, custo, tempo_conexao, escala_obrigatoria, custo_escala in voos:
    aeroporto_mapa.adicionar_voo(aeroporto1, aeroporto2, custo, tempo_conexao, escala_obrigatoria, custo_escala)

origem = "A"
destino = "E"
tempo_maximo = 6  

rota, custo_total = aeroporto_mapa.dijkstra(origem, destino, tempo_maximo)

print(f"\nMelhor rota de {origem} para {destino}: {' => '.join(rota)}")
print(f"Custo total da viagem: R${custo_total}")
