import time

def movimentos_possiveis(x, y, tabuleiro):
    movimentos = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    return [(x + dx, y + dy) for dx, dy in movimentos
            if 0 <= x + dx < len(tabuleiro) and 0 <= y + dy < len(tabuleiro[0]) and tabuleiro[x + dx][y + dy] == 0]

def movimento_menor_grau(x, y, tabuleiro):
    movimentos = movimentos_possiveis(x, y, tabuleiro)
    if not movimentos:
        return None
    return min(movimentos, key=lambda m: len(movimentos_possiveis(m[0], m[1], tabuleiro)))

def passeio_cavalo_heuristica(tamanho):
    tabuleiro = [[0] * tamanho for _ in range(tamanho)]
    x, y = 0, 0 
    tabuleiro[x][y] = 1
    for movimento in range(2, tamanho * tamanho + 1):
        proximo = movimento_menor_grau(x, y, tabuleiro)
        if proximo is None:
            return None
        x, y = proximo
        tabuleiro[x][y] = movimento
    return tabuleiro

def passeio_cavalo_forca_bruta(tabuleiro, x, y, movimento):
    if movimento == len(tabuleiro) * len(tabuleiro):
        return True
    
    for nx, ny in movimentos_possiveis(x, y, tabuleiro):
        tabuleiro[nx][ny] = movimento + 1
        if passeio_cavalo_forca_bruta(tabuleiro, nx, ny, movimento + 1):
            return True
        tabuleiro[nx][ny] = 0
    
    return False

def resolver_forca_bruta(tamanho):
    tabuleiro = [[0] * tamanho for _ in range(tamanho)]
    tabuleiro[0][0] = 1
    if passeio_cavalo_forca_bruta(tabuleiro, 0, 0, 1):
        return tabuleiro
    return None

def imprimir_tabuleiro(tabuleiro):
    if tabuleiro is None:
        print("Solução não encontrada.")
    else:
        for linha in tabuleiro:
            print(linha)

tamanhos = [5, 8]
for tamanho in tamanhos:
    print(f"\nTabuleiro {tamanho}x{tamanho} - Heurística:")
    inicio = time.time()
    solucao = passeio_cavalo_heuristica(tamanho)
    fim = time.time()
    imprimir_tabuleiro(solucao)
    print(f"Tempo: {fim - inicio:.4f} segundos")
    
    print(f"\nTabuleiro {tamanho}x{tamanho} - Força Bruta:")
    inicio = time.time()
    solucao = resolver_forca_bruta(tamanho)
    fim = time.time()
    imprimir_tabuleiro(solucao)
    print(f"Tempo: {fim - inicio:.4f} segundos")
