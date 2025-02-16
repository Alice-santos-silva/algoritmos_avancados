class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, i):
        while i > 0:
            pai = (i - 1) // 2
            if self.heap[i][0] >= self.heap[pai][0]:
                break
            self.heap[i], self.heap[pai] = self.heap[pai], self.heap[i]
            i = pai

    def _heapify_down(self, i):
        n = len(self.heap)
        while True:
            menor = i
            esq = 2 * i + 1
            dir = 2 * i + 2
            if esq < n and self.heap[esq][0] < self.heap[menor][0]:
                menor = esq
            if dir < n and self.heap[dir][0] < self.heap[menor][0]:
                menor = dir
            if menor == i:
                break
            self.heap[i], self.heap[menor] = self.heap[menor], self.heap[i]
            i = menor

heap = MinHeap()
valores = [(3, 'A'), (1, 'B'), (4, 'C'), (2, 'D')]
for v in valores:
    heap.insert(v)
    print("Após inserir:", heap.heap)

while heap.heap:
    print("Removido:", heap.pop())
    print("Estado atual:", heap.heap)
