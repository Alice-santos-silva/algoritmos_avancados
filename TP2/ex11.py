grafo = {
    'A': ['C', 'B'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

visitados = []

def dfs(grafo, vertice, visitados):
    visitados.append(vertice)
    
  
    for vizinho in grafo[vertice]:
        if vizinho not in visitados:
            dfs(grafo, vizinho, visitados)


dfs(grafo, 'A', visitados)

print("Ordem de visitação:", visitados)