def detectar_ciclos(grafo, vertice_inicial=None):
    todos_ciclos = []
    visitados = set()     
    em_exploracao = set()  
    pilha = []             
    
    def dfs(vertice):
        if vertice in em_exploracao:
            idx = pilha.index(vertice)
            ciclo = pilha[idx:]  
            todos_ciclos.append(ciclo)
            return
            
        if vertice in visitados:
            return
            
        pilha.append(vertice)
        em_exploracao.add(vertice)
        
        for vizinho in grafo.get(vertice, []):
            dfs(vizinho)
            
        pilha.pop()
        em_exploracao.remove(vertice)
        visitados.add(vertice)
    
    if vertice_inicial:
        dfs(vertice_inicial)
    else:
        for vertice in grafo:
            if vertice not in visitados:
                dfs(vertice)
    
    return todos_ciclos

if __name__ == "__main__":
    transacoes = {
        "Conta_A": ["Conta_B"],
        "Conta_B": ["Conta_C"],
        "Conta_C": ["Conta_D"],
        "Conta_D": ["Conta_A"],  
    }
    
    ciclos = detectar_ciclos(transacoes)
    print(f"Ciclos detectados: {len(ciclos)}")
    for i, ciclo in enumerate(ciclos):
        print(f"Ciclo {i+1}: {' -> '.join(ciclo)}")  
