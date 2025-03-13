from collections import deque

grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D']
}

def bfs_caminho_mais_curto(grafo, inicio, destino):
    fila = deque([inicio])  
    visitados = set([inicio])  
    pais = {inicio: None}  
    
    while fila:
        atual = fila.popleft() 
        
        if atual == destino:
            caminho = []
            while atual is not None: 
                caminho.append(atual)
                atual = pais[atual]
            return caminho[::-1]  
        
        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
                pais[vizinho] = atual  
    
    return None  

caminho = bfs_caminho_mais_curto(grafo, 'A', 'E')
print("Caminho mais curto entre A e E:", caminho)