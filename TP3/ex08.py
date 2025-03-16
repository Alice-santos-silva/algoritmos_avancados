INF = float('inf')

def floyd_warshall(grafo):
    num_bairros = len(grafo)
    
    dist = [[grafo[i][j] for j in range(num_bairros)] for i in range(num_bairros)]

    for k in range(num_bairros):  
        for i in range(num_bairros):  
            for j in range(num_bairros):  
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist  

grafo_bairros = [
    [0, 10, INF, 15, INF],  
    [10, 0, 5, INF, INF], 
    [INF, 5, 0, 8, 3],     
    [15, INF, 8, 0, 6],    
    [INF, INF, 3, 6, 0]    
]

menores_caminhos = floyd_warshall(grafo_bairros)

print("Menor caminho entre todos os pares de vértices.")
for linha in menores_caminhos:
    print(linha)
