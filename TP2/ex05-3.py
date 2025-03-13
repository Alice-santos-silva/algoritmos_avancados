grafo_ponderado = {
    'A': {'B': 10, 'C': 20},
    'B': {'A': 10, 'D': 15},
    'C': {'A': 20, 'E': 25},
    'D': {'B': 15, 'E': 5},
    'E': {'C': 25, 'D': 5}
}

for centro, vizinhos in grafo_ponderado.items():
    for vizinho, peso in vizinhos.items():
        print(f'{centro} está conectado a {vizinho} com tempo de {peso} minutos')