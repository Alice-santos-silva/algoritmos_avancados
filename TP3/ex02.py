class MapaCidade:
    def __init__(self):
        self.bairros = {}

    def adicionar_bairro(self, bairro):
        if bairro not in self.bairros:
            self.bairros[bairro] = {}

    def adicionar_rua(self, bairro1, bairro2, tempo):
        self.bairros[bairro1][bairro2] = tempo
        self.bairros[bairro2][bairro1] = tempo

    def caminho_rapido(self, inicio, fim):
        nao_visitados = list(self.bairros.keys())
        tempos = {b: float("inf") for b in self.bairros}
        tempos[inicio] = 0
        anteriores = {}

        while nao_visitados:
            atual = min(nao_visitados, key=lambda b: tempos[b])
            if tempos[atual] == float("inf"):
                break
            
            for vizinho, tempo in self.bairros[atual].items():
                novo_tempo = tempos[atual] + tempo
                if novo_tempo < tempos[vizinho]:
                    tempos[vizinho] = novo_tempo
                    anteriores[vizinho] = atual
            
            nao_visitados.remove(atual)

        trajeto = []
        bairro_atual = fim
        while bairro_atual in anteriores:
            trajeto.append(bairro_atual)
            bairro_atual = anteriores[bairro_atual]
        trajeto.append(inicio)
        trajeto.reverse()

        return trajeto, tempos[fim]

cidade = MapaCidade()
bairros = ["Méier", "Tijuca", "Madureira", "Penha", "Engenho de Dentro", "Vila Isabel", "Manguinhos"]

for bairro in bairros:
    cidade.adicionar_bairro(bairro)

ruas = [
    ("Méier", "Tijuca", 4), ("Méier", "Madureira", 3),
    ("Tijuca", "Madureira", 5), ("Tijuca", "Penha", 2),
    ("Madureira", "Engenho de Dentro", 7), ("Penha", "Engenho de Dentro", 6),
    ("Penha", "Vila Isabel", 5), ("Engenho de Dentro", "Vila Isabel", 2),
    ("Vila Isabel", "Manguinhos", 3)
]

for bairro1, bairro2, tempo in ruas:
    cidade.adicionar_rua(bairro1, bairro2, tempo)

inicio, fim = "Méier", "Manguinhos"
rota, tempo_total = cidade.caminho_rapido(inicio, fim)

print(f"\nPercurso mais rápido de {inicio} para {fim}: {' => '.join(rota)}")
print(f"Tempo total: {tempo_total} min")
