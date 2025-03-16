class MapaLogistico:
    def __init__(self):
        self.bairros = {}

    def adicionar_bairro(self, bairro):
        if bairro not in self.bairros:
            self.bairros[bairro] = {}

    def adicionar_rua(self, bairro1, bairro2, distancia):
        self.bairros[bairro1][bairro2] = distancia
        self.bairros[bairro2][bairro1] = distancia 

    def dijkstra(self, origem):
        nao_visitados = list(self.bairros.keys())
        distancias = {bairro: float("inf") for bairro in self.bairros}
        distancias[origem] = 0
        caminho_anterior = {}

        while nao_visitados:
            bairro_atual = min(nao_visitados, key=lambda bairro: distancias[bairro])
            if distancias[bairro_atual] == float("inf"):
                break

            for vizinho, distancia in self.bairros[bairro_atual].items():
                nova_distancia = distancias[bairro_atual] + distancia
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    caminho_anterior[vizinho] = bairro_atual

            nao_visitados.remove(bairro_atual)

        return distancias, caminho_anterior

    def rota_para(self, origem, destino, caminho_anterior):
        caminho = []
        bairro_atual = destino
        while bairro_atual in caminho_anterior:
            caminho.append(bairro_atual)
            bairro_atual = caminho_anterior[bairro_atual]
        caminho.append(origem)
        caminho.reverse()
        return caminho

mapa = MapaLogistico()
bairros = ["Méier", "Tijuca", "Madureira", "Penha", "Engenho de Dentro", "Vila Isabel", "Manguinhos"]

for bairro in bairros:
    mapa.adicionar_bairro(bairro)

ruas = [
    ("Méier", "Tijuca", 4), ("Méier", "Madureira", 3),
    ("Tijuca", "Madureira", 5), ("Tijuca", "Penha", 2),
    ("Madureira", "Engenho de Dentro", 7), ("Penha", "Engenho de Dentro", 6),
    ("Penha", "Vila Isabel", 5), ("Engenho de Dentro", "Vila Isabel", 2),
    ("Vila Isabel", "Manguinhos", 3)
]

for bairro1, bairro2, distancia in ruas:
    mapa.adicionar_rua(bairro1, bairro2, distancia)

distancias, caminho_anterior = mapa.dijkstra("Méier")

print("\nRotas mais rápidas a partir do Méier:")
for bairro in bairros:
    if bairro != "Méier":
        caminho = mapa.rota_para("Méier", bairro, caminho_anterior)
        print(f"- Para {bairro}: {' => '.join(caminho)} (Distância: {distancias[bairro]} km)")
