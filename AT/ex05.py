from collections import deque

grafo_metro = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'E'],
    'E': ['B', 'D', 'F'],
    'F': ['C', 'E']
}

def dfs(grafo, inicio):
    visitados = []
    
    def dfs_recursivo(grafo, vertice, visitados):
        visitados.append(vertice)
        
        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                dfs_recursivo(grafo, vizinho, visitados)
    
    dfs_recursivo(grafo, inicio, visitados)
    return visitados

def bfs(grafo, inicio):
    visitados = []
    fila = deque([inicio])
    estacoes_visitadas = set([inicio])
    
    while fila:
        atual = fila.popleft()
        visitados.append(atual)
        
        for vizinho in grafo[atual]:
            if vizinho not in estacoes_visitadas:
                estacoes_visitadas.add(vizinho)
                fila.append(vizinho)
    
    return visitados

ordem_dfs = dfs(grafo_metro, 'A')
ordem_bfs = bfs(grafo_metro, 'A')

print("Ordem de visitação DFS:", ordem_dfs)
print("Ordem de visitação BFS:", ordem_bfs)
print(f"DFS: {ordem_dfs}")
print(f"BFS: {ordem_bfs}")
