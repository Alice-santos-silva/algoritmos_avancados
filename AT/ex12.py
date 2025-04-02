import random
import time

def distancia(c1, c2):
    return ((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2) ** 0.5

def gerar_cidades(n):
    return {i: (random.randint(0, 100), random.randint(0, 100)) for i in range(n)}

def held_karp(cidades):
    n = len(cidades)
    dp = {}
    
    def tsp(mask, pos):
        if mask == (1 << n) - 1:
            return distancia(cidades[pos], cidades[0])
        if (mask, pos) in dp:
            return dp[(mask, pos)]
        
        res = float('inf')
        for prox in range(n):
            if mask & (1 << prox) == 0:
                res = min(res, distancia(cidades[pos], cidades[prox]) + tsp(mask | (1 << prox), prox))
        dp[(mask, pos)] = res
        return res
    
    return tsp(1, 0)

def vizinho_mais_proximo(cidades):
    n = len(cidades)
    inicio = list(cidades.keys())[0]
    caminho, visitados = [inicio], {inicio}
    while len(caminho) < n:
        ultimo = caminho[-1]
        prox = min((c for c in cidades if c not in visitados), key=lambda c: distancia(cidades[ultimo], cidades[c]))
        visitados.add(prox)
        caminho.append(prox)
    return sum(distancia(cidades[caminho[i]], cidades[caminho[i+1]]) for i in range(n-1)) + distancia(cidades[caminho[-1]], cidades[caminho[0]]), caminho

def algoritmo_genetico(cidades, tam_pop=100, geracoes=500, taxa_mutacao=0.1):
    def avaliar(caminho):
        return sum(distancia(cidades[caminho[i]], cidades[caminho[i+1]]) for i in range(len(caminho)-1)) + distancia(cidades[caminho[-1]], cidades[caminho[0]])
    
    def mutacao(caminho):
        if random.random() < taxa_mutacao:
            i, j = random.sample(range(len(caminho)), 2)
            caminho[i], caminho[j] = caminho[j], caminho[i]
        return caminho
    
    def crossover(p1, p2):
        corte = random.randint(1, len(p1)-2)
        filho = p1[:corte] + [c for c in p2 if c not in p1[:corte]]
        return filho
    
    pop = [random.sample(list(cidades.keys()), len(cidades)) for _ in range(tam_pop)]
    for _ in range(geracoes):
        pop = sorted(pop, key=avaliar)
        nova_pop = pop[:10] + [mutacao(crossover(random.choice(pop[:50]), random.choice(pop[:50]))) for _ in range(tam_pop - 10)]
        pop = nova_pop
    melhor = min(pop, key=avaliar)
    return avaliar(melhor), melhor

cidades = gerar_cidades(5)

start = time.time()
resultado_hk = held_karp(cidades)
print("Held-Karp:", resultado_hk, "Tempo:", time.time() - start)

start = time.time()
resultado_vn = vizinho_mais_proximo(cidades)
print("Vizinho Mais Próximo:", resultado_vn, "Tempo:", time.time() - start)

start = time.time()
resultado_ag = algoritmo_genetico(cidades)
print("Algoritmo Genético:", resultado_ag, "Tempo:", time.time() - start)
