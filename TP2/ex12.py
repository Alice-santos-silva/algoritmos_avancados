from collections import deque

def bfs_caminho_mais_curto(grafo, inicio, destino):
    fila = deque([inicio])
    visitados = set([inicio])
    
    pais = {inicio: None}
    
    ordem_visitada = []
    
    while fila:
        atual = fila.popleft()
        
        ordem_visitada.append(atual)
        
        if atual == destino:
            caminho = []
            while atual is not None:
                caminho.append(atual)
                atual = pais[atual]
            return ordem_visitada, caminho[::-1]  
        
        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
                pais[vizinho] = atual
    
    return ordem_visitada, None

grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

ordem_visitada, caminho = bfs_caminho_mais_curto(grafo, 'A', 'F')

if caminho:
    print("Ordem dos bairros visitados:", ordem_visitada)
    print("Caminho mais curto de A a F:", caminho)
else:
    print("Não há caminho de A a F.")