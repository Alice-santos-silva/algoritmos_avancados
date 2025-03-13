grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D']
}

for centro, vizinhos in grafo.items():
    print(f'{centro} tem vizinhos: {vizinhos}')