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

    def hierarquia(self, node=None, nivel=0):
        if node is None:
            node = self.root
        for char, child in node.children.items():
            print("  " * nivel + "- " + char)
            self.hierarquia(child, nivel + 1)

trie = Trie()
for palavra in ["casa", "carro", "caminhão", "cachorro", "cadeira"]:
    trie.insert(palavra)

trie.hierarquia()
