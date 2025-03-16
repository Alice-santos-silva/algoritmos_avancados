class GrafoPoderado:
    def __init__(self):
        self.vertices = {}

    def adicionar_cidade(self, cidade):
        if cidade not in self.vertices:
            self.vertices[cidade] = {}

    def adicionar_estrada(self, cidade1, cidade2, custo):
        self.vertices[cidade1][cidade2] = custo
        self.vertices[cidade2][cidade1] = custo

    def dijkstra(self, origem, destino):
        nao_visitados = list(self.vertices.keys())
        custos = {cidade: float("inf") for cidade in self.vertices}
        custos[origem] = 0
        predecessores = {}

        while nao_visitados:
            cidade_atual = min(nao_visitados, key=lambda cidade: custos[cidade])
            if custos[cidade_atual] == float("inf"):
                break

            for vizinho, custo in self.vertices[cidade_atual].items():
                novo_custo = custos[cidade_atual] + custo
                if novo_custo < custos[vizinho]:
                    custos[vizinho] = novo_custo
                    predecessores[vizinho] = cidade_atual

            nao_visitados.remove(cidade_atual)

        caminho = []
        cidade_atual = destino
        while cidade_atual in predecessores:
            caminho.append(cidade_atual)
            cidade_atual = predecessores[cidade_atual]
        caminho.append(origem)
        caminho.reverse()

        return caminho, custos[destino]

mapa_cidades = GrafoPoderado()
cidades = ["Rio", "São Paulo", "Campinas", "Belo Horizonte", "Curitiba", "Florianópolis", "Porto Alegre"]

for cidade in cidades:
    mapa_cidades.adicionar_cidade(cidade)

estradas = [
    ("Rio", "São Paulo", 100), ("Rio", "Belo Horizonte", 120),
    ("São Paulo", "Campinas", 50), ("Campinas", "Curitiba", 80),
    ("Belo Horizonte", "Curitiba", 150), ("Curitiba", "Florianópolis", 110),
    ("Florianópolis", "Porto Alegre", 130)
]

for cidade1, cidade2, custo in estradas:
    mapa_cidades.adicionar_estrada(cidade1, cidade2, custo)

origem = "Rio"
destino = "São Paulo"
rota, custo_total = mapa_cidades.dijkstra(origem, destino)

print(f"\nMelhor rota de {origem} para {destino}: {' => '.join(rota)}")
print(f"Custo total: {custo_total}")
