class TransferAereo:
    def __init__(self):
        self.aeroportos = {}

    def adicionar_aeroporto(self, ap):
        if ap not in self.aeroportos:
            self.aeroportos[ap] = {}

    def adicionar_rota(self, ap1, ap2, dist):
        self.aeroportos[ap1][ap2] = dist
        self.aeroportos[ap2][ap1] = dist

    def menor_rota(self, origem, destino):
        nao_visitados = list(self.aeroportos.keys())
        distancias = {ap: float("inf") for ap in self.aeroportos}
        distancias[origem] = 0
        predecessores = {}

        while nao_visitados:
            atual = min(nao_visitados, key=lambda ap: distancias[ap])
            if distancias[atual] == float("inf"):
                break
            for vizinho, dist in self.aeroportos[atual].items():
                nova_dist = distancias[atual] + dist
                if nova_dist < distancias[vizinho]:
                    distancias[vizinho] = nova_dist
                    predecessores[vizinho] = atual
            nao_visitados.remove(atual)

        caminho = []
        ap_atual = destino
        while ap_atual in predecessores:
            caminho.append(ap_atual)
            ap_atual = predecessores[ap_atual]
        caminho.append(origem)
        caminho.reverse()

        return caminho, distancias[destino]

mapa = TransferAereo()
aeroportos = ["GRU", "GIG", "BSB", "CGH", "POA", "SSA", "REC"]

for ap in aeroportos:
    mapa.adicionar_aeroporto(ap)

rotas = [
    ("GRU", "GIG", 400), ("GRU", "BSB", 850),
    ("GIG", "SSA", 1200), ("BSB", "CGH", 870),
    ("CGH", "POA", 850), ("SSA", "REC", 675),
    ("POA", "REC", 3000)
]

for ap1, ap2, dist in rotas:
    mapa.adicionar_rota(ap1, ap2, dist)

origem, destino = "GRU", "REC"
caminho, distancia = mapa.menor_rota(origem, destino)

print(f"\nMelhor rota de {origem} para {destino}: {' => '.join(caminho)}")
print(f"Distância total: {distancia} km")
