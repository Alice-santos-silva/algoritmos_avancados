from collections import deque

grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['C', 'F'],
    'F': ['D', 'E']
}

def bfs(grafo, inicio):
    fila = deque([inicio])  
    visitados = set([inicio])  
    ordem = []  
    
    while fila:
        vertice_atual = fila.popleft()  
        ordem.append(vertice_atual)  
        
        for vizinho in grafo[vertice_atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)  
                fila.append(vizinho) 
    
    return ordem

ordem_visitados = bfs(grafo, 'A')

print("Ordem dos vértices visitados pela BFS:", ordem_visitados)