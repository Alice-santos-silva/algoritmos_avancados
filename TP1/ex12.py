class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        def _collect_words(n, pref):
            palavras = []
            if n.is_end_of_word:
                palavras.append(pref)
            for ch, child in n.children.items():
                palavras.extend(_collect_words(child, pref + ch))
            return palavras
        
        return _collect_words(node, prefix)

dados = Trie()
for palavra in ["cama", "travesseiro", "lençol", "colcha", "edredom", "cortina"]:
    dados.insert(palavra)

while True:
    prefixo = input("Digite um prefixo para filtrar (ou 'sair' para encerrar): ")
    if prefixo.lower() == 'sair':
        break
    resultados = dados.starts_with(prefixo)
    print("Resultados encontrados:", resultados if resultados else "Nenhum resultado.")
