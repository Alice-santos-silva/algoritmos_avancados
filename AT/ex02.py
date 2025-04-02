class PacoteRede:
    def __init__(self, id_pacote, prioridade, tempo_transmissao):
        self.id = id_pacote
        self.prioridade = prioridade
        self.tempo_transmissao = tempo_transmissao
    
    def __str__(self):
        return f"Pacote ID: {self.id}, Prioridade: {self.prioridade}, Tempo: {self.tempo_transmissao}ms"

class HeapMinimoPacotes:
    def __init__(self):
        self.heap = []
        self.mapa_posicoes = {}
    
    def tamanho(self):
        return len(self.heap)
    
    def esta_vazio(self):
        return len(self.heap) == 0
    
    def _trocar(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.mapa_posicoes[self.heap[i].id] = i
        self.mapa_posicoes[self.heap[j].id] = j
    
    def _subir(self, indice):
        pai = (indice - 1) // 2
        
        if indice > 0 and self.heap[indice].prioridade < self.heap[pai].prioridade:
            self._trocar(indice, pai)
            self._subir(pai)
    
    def _descer(self, indice):
        menor = indice
        esquerdo = 2 * indice + 1
        direito = 2 * indice + 2
        tamanho = len(self.heap)
        
        if esquerdo < tamanho and self.heap[esquerdo].prioridade < self.heap[menor].prioridade:
            menor = esquerdo
            
        if direito < tamanho and self.heap[direito].prioridade < self.heap[menor].prioridade:
            menor = direito
            
        if menor != indice:
            self._trocar(indice, menor)
            self._descer(menor)
    
    def inserir(self, pacote):
        self.heap.append(pacote)
        indice = len(self.heap) - 1
        self.mapa_posicoes[pacote.id] = indice
        self._subir(indice)
        
    def remover_maior_prioridade(self):
        if self.esta_vazio():
            return None
            
        pacote_maior_prioridade = self.heap[0]
        ultimo_pacote = self.heap.pop()
        
        if self.heap:
            self.heap[0] = ultimo_pacote
            self.mapa_posicoes[ultimo_pacote.id] = 0
            self._descer(0)
            
        del self.mapa_posicoes[pacote_maior_prioridade.id]
        return pacote_maior_prioridade
    
    def atualizar_prioridade(self, id_pacote, nova_prioridade):
        if id_pacote not in self.mapa_posicoes:
            return False
            
        indice = self.mapa_posicoes[id_pacote]
        prioridade_antiga = self.heap[indice].prioridade
        self.heap[indice].prioridade = nova_prioridade
        
        if nova_prioridade < prioridade_antiga:
            self._subir(indice)
        elif nova_prioridade > prioridade_antiga:
            self._descer(indice)
            
        return True
    
    def visualizar_heap(self):
        return [str(pacote) for pacote in self.heap]

def demonstrar_sistema():
    gerenciador = HeapMinimoPacotes()
    
    pacotes = [
        PacoteRede(1, 5, 10),
        PacoteRede(2, 3, 15),
        PacoteRede(3, 7, 5),
        PacoteRede(4, 1, 20),
        PacoteRede(5, 4, 8)
    ]
    
    for pacote in pacotes:
        gerenciador.inserir(pacote)
        print(f"Inserido: {pacote}")
    
    print("\nEstado atual do heap")
    for pacote in gerenciador.visualizar_heap():
        print(pacote)
    
    print("\nRemovendo pacotes em ordem de prioridade ")
    pacote_removido = gerenciador.remover_maior_prioridade()
    print(f"Pacote removido: {pacote_removido}")
    
    print("\n Heap depois da remoção")
    for pacote in gerenciador.visualizar_heap():
        print(pacote)
    
    print("\n Prioridade do pacote ID 3 modificada")
    gerenciador.atualizar_prioridade(3, 2)
    
    print("\n Heap depois da atualização")
    for pacote in gerenciador.visualizar_heap():
        print(pacote)
    
    print("\n Pacotes restantes")
    while not gerenciador.esta_vazio():
        pacote = gerenciador.remover_maior_prioridade()
        print(pacote)


if __name__ == "__main__":
    demonstrar_sistema()
   