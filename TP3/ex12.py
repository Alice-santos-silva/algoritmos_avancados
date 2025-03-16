import time

INF = float('inf')

grafo1 = [
    [0, 3, INF, 7],
    [3, 0, 2, INF],
    [INF, 2, 0, 5],
    [7, INF, 5, 0]
]

grafo2 = [
    [0, 1, 4, INF],
    [1, 0, 2, INF],
    [4, 2, 0, 3],
    [INF, INF, 3, 0]
]

grafo3 = [
    [0, 5, INF, INF],
    [5, 0, 1, INF],
    [INF, 1, 0, 2],
    [INF, INF, 2, 0]
]

grafo4 = [
    [0, 2, 6, INF],
    [2, 0, 3, 8],
    [6, 3, 0, 1],
    [INF, 8, 1, 0]
]

def floyd_warshall(grafo):
    n = len(grafo)
    dist = [linha[:] for linha in grafo]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

def dijkstra(grafo, origem):
    n = len(grafo)
    dist = [INF] * n
    dist[origem] = 0
    visitados = set()
    while len(visitados) < n:
        u = min((v for v in range(n) if v not in visitados), key=lambda v: dist[v], default=None)
        if u is None or dist[u] == INF:
            break
        visitados.add(u)
        for v in range(n):
            if grafo[u][v] != INF and v not in visitados:
                dist[v] = min(dist[v], dist[u] + grafo[u][v])
    return dist

def comparar_algoritmos(grafo):
    inicio = time.time()
    floyd_warshall(grafo)
    tempo_fw = time.time() - inicio
    
    inicio = time.time()
    for i in range(len(grafo)):
        dijkstra(grafo, i)
    tempo_dijkstra = time.time() - inicio
    
    print(f"Floyd-Warshall: {tempo_fw:.6f} segundos")
    print(f"Dijkstra (para todos os vértices): {tempo_dijkstra:.6f} segundos")
    print("-" * 40)

print("Grafo 1:")
comparar_algoritmos(grafo1)
print("Grafo 2:")
comparar_algoritmos(grafo2)
print("Grafo 3:")
comparar_algoritmos(grafo3)
print("Grafo 4:")
comparar_algoritmos(grafo4)
