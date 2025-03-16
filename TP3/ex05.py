class GrafoPoderado:
    def __init__(self):
        self.vertices = {}

    def adicionar_cruzamento(self, cruzamento):
        if cruzamento not in self.vertices:
            self.vertices[cruzamento] = {}

    def adicionar_rua(self, cruzamento1, cruzamento2, tempo, recarga=False):
        self.vertices[cruzamento1][cruzamento2] = {'tempo': tempo, 'recarga': recarga}
        self.vertices[cruzamento2][cruzamento1] = {'tempo': tempo, 'recarga': recarga}

    def dijkstra(self, origem, destino, autonomia):
        tempos = {c: float("inf") for c in self.vertices}
        tempos[origem] = 0
        predecessores = {}
        autonomias_restantes = {c: autonomia for c in self.vertices}
        visitados = set()

        while len(visitados) < len(self.vertices):
            cruzamento_atual = None
            menor_tempo = float("inf")
            for c in self.vertices:
                if c not in visitados and tempos[c] < menor_tempo:
                    menor_tempo = tempos[c]
                    cruzamento_atual = c

            if cruzamento_atual is None or tempos[cruzamento_atual] == float("inf"):
                break

            visitados.add(cruzamento_atual)

            if cruzamento_atual == destino:
                break

            for vizinho, atributos in self.vertices[cruzamento_atual].items():
                tempo = atributos['tempo']
                precisa_recarregar = atributos['recarga']
                nova_autonomia = autonomias_restantes[cruzamento_atual] - tempo

                if nova_autonomia >= 0 or precisa_recarregar:
                    nova_distancia = tempos[cruzamento_atual] + tempo
                    if nova_distancia < tempos[vizinho]:
                        tempos[vizinho] = nova_distancia
                        predecessores[vizinho] = cruzamento_atual
                        autonomias_restantes[vizinho] = autonomia if precisa_recarregar else nova_autonomia

        caminho = []
        cruzamento_atual = destino
        while cruzamento_atual != origem:
            if cruzamento_atual not in predecessores:
                return None, float("inf")  
            caminho.append(cruzamento_atual)
            cruzamento_atual = predecessores[cruzamento_atual]
        caminho.append(origem)
        caminho.reverse()

        return caminho, tempos[destino]

mapa_cidade = GrafoPoderado()
cruzamentos = ["A", "B", "C", "D", "E", "F", "G"]
for cruzamento in cruzamentos:
    mapa_cidade.adicionar_cruzamento(cruzamento)

ruas = [
    ("A", "B", 4, False), ("A", "C", 3, False),
    ("B", "C", 5, False), ("B", "D", 2, False),
    ("C", "E", 7, False), ("D", "E", 6, False),
    ("D", "F", 5, True),  
    ("E", "F", 2, False),
    ("F", "G", 3, False)
]
for c1, c2, tempo, recarga in ruas:
    mapa_cidade.adicionar_rua(c1, c2, tempo, recarga)

origem = "A"
destino = "F"
autonomia = 8
rota, tempo = mapa_cidade.dijkstra(origem, destino, autonomia)

if rota:
    print(f"\nMelhor rota de {origem} para {destino}: {' => '.join(rota)}")
    print(f"Tempo total: {tempo} minutos")
else:
    print(f"\nNão há caminho viável de {origem} para {destino} com essa autonomia.")
