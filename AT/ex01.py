class Processo:
    def __init__(self, id, tempo_execucao, prioridade):
        self.id = id
        self.tempo_execucao = tempo_execucao
        self.prioridade = prioridade
    
    def __str__(self):
        return f"Processo ID: {self.id}, Tempo: {self.tempo_execucao}, Prioridade: {self.prioridade}"

class FilaPrioridade:
    def __init__(self):
        self.heap = []
        self.posicoes = {}
    
    def esta_vazia(self):
        return len(self.heap) == 0
    
    def pai(self, i):
        return (i - 1) // 2
    
    def filho_esquerdo(self, i):
        return 2 * i + 1
    
    def filho_direito(self, i):
        return 2 * i + 2
    
    def troca(self, i, j):
        self.posicoes[self.heap[i].id] = j
        self.posicoes[self.heap[j].id] = i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def subir_heap(self, i):
        pai = self.pai(i)
        if i > 0 and self.heap[i].prioridade < self.heap[pai].prioridade:
            self.troca(i, pai)
            self.subir_heap(pai)
    
    def descer_heap(self, i):
        menor = i
        esq = self.filho_esquerdo(i)
        dir = self.filho_direito(i)
        
        if esq < len(self.heap) and self.heap[esq].prioridade < self.heap[menor].prioridade:
            menor = esq
        
        if dir < len(self.heap) and self.heap[dir].prioridade < self.heap[menor].prioridade:
            menor = dir
        
        if menor != i:
            self.troca(i, menor)
            self.descer_heap(menor)
    
    def adicionar_processo(self, processo):
        self.heap.append(processo)
        indice = len(self.heap) - 1
        self.posicoes[processo.id] = indice
        self.subir_heap(indice)
        print(f"Processo {processo.id} adicionado com prioridade {processo.prioridade}")
    
    def executar_proximo_processo(self):
        if self.esta_vazia():
            print("Não há processos para executar")
            return None
        
        processo = self.heap[0]
        ultimo_processo = self.heap.pop()
        
        del self.posicoes[processo.id]
        
        if self.heap:
            self.heap[0] = ultimo_processo
            self.posicoes[ultimo_processo.id] = 0
            self.descer_heap(0)
        
        print(f"Executando processo {processo.id} com prioridade {processo.prioridade}")
        return processo
    
    def modificar_prioridade(self, id, nova_prioridade):
        if id not in self.posicoes:
            print(f"Processo {id} não encontrado")
            return
        
        indice = self.posicoes[id]
        prioridade_antiga = self.heap[indice].prioridade
        self.heap[indice].prioridade = nova_prioridade
        
        print(f"Prioridade do processo {id} modificada de {prioridade_antiga} para {nova_prioridade}")
        
        if nova_prioridade < prioridade_antiga:
            self.subir_heap(indice)
        else:
            self.descer_heap(indice)
    
    def mostrar_processos(self):
        if self.esta_vazia():
            print("Não há processos na fila")
        else:
            print("Processos na fila (por ordem de prioridade):")
            for processo in self.heap:
                print(processo)

if __name__ == "__main__":
    escalonador = FilaPrioridade()
    
    escalonador.adicionar_processo(Processo(1, 10, 3))
    escalonador.adicionar_processo(Processo(2, 5, 1))
    escalonador.adicionar_processo(Processo(3, 8, 4))
    escalonador.adicionar_processo(Processo(4, 3, 2))
    
    print("\nListando todos os processos:")
    escalonador.mostrar_processos()
    
    print("\nExecutando processos:")
    escalonador.executar_proximo_processo()
    escalonador.mostrar_processos()
    
    print("\nModificando prioridade:")
    escalonador.modificar_prioridade(3, 0)
    escalonador.mostrar_processos()
    
    print("\nExecutando o restante dos processos:")
    while not escalonador.esta_vazia():
        escalonador.executar_proximo_processo()