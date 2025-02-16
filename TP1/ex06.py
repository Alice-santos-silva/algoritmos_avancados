class MinHeap:
    def __init__(self):
        self.heap = []

    def _heapify(self, indice, tamanho):
        menor = indice
        esq = 2 * indice + 1  
        dir = 2 * indice + 2  

        if esq < tamanho and self.heap[esq][1] < self.heap[menor][1]:
            menor = esq
        if dir < tamanho and self.heap[dir][1] < self.heap[menor][1]:
            menor = dir

        if menor != indice:
            self.heap[indice], self.heap[menor] = self.heap[menor], self.heap[indice]
            self._heapify(menor, tamanho)

    def inserir(self, nome, prioridade):
        self.heap.append((nome, prioridade))
        indice = len(self.heap) - 1

        while indice > 0:
            pai = (indice - 1) // 2
            if self.heap[indice][1] < self.heap[pai][1]:
                self.heap[indice], self.heap[pai] = self.heap[pai], self.heap[indice]
                indice = pai
            else:
                break

    def remover(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._heapify(0, len(self.heap))

        return raiz

    def esta_vazia(self):
        return len(self.heap) == 0

    def ordenar(self):
        resultado = []
        while not self.esta_vazia():
            resultado.append(self.remover())
        return resultado


def solicitar_dados():
    fila = MinHeap()
    
    while True:
        tarefa = input("Digite a tarefa (ou 'sair' para finalizar): ")
        if tarefa.lower() == 'sair':
            break
        try:
            prioridade = int(input(f"Digite a prioridade da tarefa: {tarefa}: "))
            fila.inserir(tarefa, prioridade)
        except ValueError:
            print("Por favor, insira um número válido para a prioridade.")

    ordenados = fila.ordenar()

    print("\nFila de Prioridade Ordenada (do menor para o maior):")
    for item in ordenados:
        print(f"Tarefa: {item[0]}, Prioridade: {item[1]}")

    input("\nPressione Enter para sair...")

if __name__ == "__main__":
    solicitar_dados()