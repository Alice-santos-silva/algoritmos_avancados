class TrieNode:
    def __init__(self):
        self.filhos = {}
        self.fim_de_palavra = False

class Trie:
    def __init__(self):
        self.raiz = TrieNode()

    def inserir(self, palavra):
        no = self.raiz
        for char in palavra:
            if char not in no.filhos:
                no.filhos[char] = TrieNode()
            no = no.filhos[char]
        no.fim_de_palavra = True

    def buscar(self, palavra):
        no = self.raiz
        for char in palavra:
            if char not in no.filhos:
                return False
            no = no.filhos[char]
        return no.fim_de_palavra

    def comeca_com(self, prefixo):
        no = self.raiz
        for char in prefixo:
            if char not in no.filhos:
                return False
            no = no.filhos[char]
        return True

    def deletar(self, palavra):
        def _deletar(no, palavra, profundidade):
            if profundidade == len(palavra):
                if not no.fim_de_palavra:
                    return False
                no.fim_de_palavra = False
                return len(no.filhos) == 0

            char = palavra[profundidade]
            if char not in no.filhos:
                return False

            deve_deletar_filho = _deletar(no.filhos[char], palavra, profundidade + 1)

            if deve_deletar_filho:
                del no.filhos[char]
                return len(no.filhos) == 0 and not no.fim_de_palavra

            return False

        _deletar(self.raiz, palavra, 0)

    def listar_palavras(self):
        def _busca_profunda(no, prefixo, palavras):
            if no.fim_de_palavra:
                palavras.append(prefixo)
            for char, filho in no.filhos.items():
                _busca_profunda(filho, prefixo + char, palavras)

        palavras = []
        _busca_profunda(self.raiz, "", palavras)
        return palavras

    def autocompletar(self, prefixo):
        no = self.raiz
        for char in prefixo:
            if char not in no.filhos:
                return []
            no = no.filhos[char]
        
        sugestoes = []
        def coletar_palavras(no, palavra_atual):
            if no.fim_de_palavra:
                sugestoes.append(palavra_atual)
            
            for char, filho in no.filhos.items():
                coletar_palavras(filho, palavra_atual + char)
        
        coletar_palavras(no, prefixo)
        return sugestoes

    def distancia_levenshtein(self, palavra1, palavra2):
        m, n = len(palavra1), len(palavra2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if palavra1[i - 1] == palavra2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        
        return dp[m][n]

    def corrigir_palavra(self, palavra, distancia_maxima=2):
        todas_palavras = self.listar_palavras()
        candidatos_correcao = []
        
        for candidato in todas_palavras:
            distancia = self.distancia_levenshtein(palavra, candidato)
            if distancia <= distancia_maxima:
                candidatos_correcao.append((candidato, distancia))
        
        if not candidatos_correcao:
            return []
        
        candidatos_correcao.sort(key=lambda x: x[1])
        return [palavra for palavra, _ in candidatos_correcao]

class SistemaBuscaLivros:
    def __init__(self):
        self.trie = Trie()
    
    def adicionar_livro(self, titulo):
        palavras = titulo.lower().split()
        for palavra in palavras:
            self.trie.inserir(palavra)
    
    def sugestao_autocompletar(self, prefixo):
        prefixo = prefixo.lower()
        return self.trie.autocompletar(prefixo)
    
    def sugestao_correcao(self, palavra, distancia_maxima=2):
        palavra = palavra.lower()
        return self.trie.corrigir_palavra(palavra, distancia_maxima)

sistema_busca = SistemaBuscaLivros()

titulos_livros = [
    "A biblioteca da meia noite",
    "O Peregrino",
    "Comer , rezar, amar",
    "Como eu era antes de você",
]

for titulo in titulos_livros:
    sistema_busca.adicionar_livro(titulo)

prefixo = "pe"
resultados_autocompletar = sistema_busca.sugestao_autocompletar(prefixo)
print(f"Sugestões de autocompletar para '{prefixo}': {resultados_autocompletar}")

palavra_errada = "bliblioteca"
resultados_correcao = sistema_busca.sugestao_correcao(palavra_errada)
print(f"Correções sugeridas para '{palavra_errada}': {resultados_correcao}")
