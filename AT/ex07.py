import numpy as np

n = 6
bairros = ['A', 'B', 'C', 'D', 'E', 'F']

INF = float('inf')
dist = np.full((n, n), INF)

for i in range(n):
    dist[i][i] = 0

arestas = [
    (0, 1, 5), (0, 2, 10), (1, 2, 3), (1, 3, 8),
    (2, 3, 2), (2, 4, 7), (3, 4, 4), (3, 5, 6), (4, 5, 5)
]

for u, v, peso in arestas:
    dist[u][v] = peso
    dist[v][u] = peso

def imprimir_matriz(titulo, matriz):
    print(f"\n{titulo}:")
    print("\t" + "\t".join(bairros))
    for i in range(n):
        linha = [bairros[i]] + [str(int(matriz[i][j])) if matriz[i][j] != INF else "S/C" for j in range(n)]
        print("\t".join(linha))

imprimir_matriz("Matriz de adjacência inicial", dist)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] != INF and dist[k][j] != INF:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

imprimir_matriz("Menores tempos de deslocamento entre bairros", dist)

print(f"\nTempo mais curto de {bairros[0]} até {bairros[-1]}: {int(dist[0][-1])} minutos")