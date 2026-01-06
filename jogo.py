from random import choice
from configuracoes import TAMANHO_MATRIZ, LETRAS

def gerar_matriz():
    # cada linha da matriz é um list comprehension da constante LETRAS
    matriz = [[choice(LETRAS) for i in range(TAMANHO_MATRIZ)]
              for j in range(TAMANHO_MATRIZ)]
    return matriz

# aqui o resultado deve ser um booleano para confirmar a adição
def cabe_na_matriz(palavra, direcao, linha, coluna):
    if direcao == "horizontal":
        return coluna + len(palavra) <= TAMANHO_MATRIZ
    if direcao == "vertical":
        return linha + len(palavra) <= TAMANHO_MATRIZ
    return False

# e aqui a palavra é de fato adicionada à matriz
def adicionar_palavra(matriz, palavra, direcao, linha, coluna):
    if not cabe_na_matriz(palavra, direcao, linha, coluna):
        return 
    
    for i, letra in enumerate(palavra):
        if direcao == "horizontal":
            # percorre as colunas de uma em uma
            matriz[linha][coluna + i] = letra
        elif direcao == "vertical":
            # percorre as linhas de uma em uma
            matriz[linha + i][coluna] = letra

# variações dos jogos que serão escolhidas aleatoriamente
def jogo_verao_hardware(matriz):
    adicionar_palavra(matriz, "PLACA", "horizontal", 0, 0)
    adicionar_palavra(matriz, "FONTE", "vertical", 0, 6)
    adicionar_palavra(matriz, "MEMÓRIA", "horizontal", 2, 10)
    adicionar_palavra(matriz, "PROCESSADOR", "vertical", 1, 14)
    adicionar_palavra(matriz, "DISCO", "horizontal", 5, 0)
    adicionar_palavra(matriz, "TECLADO", "vertical", 7, 3)
    adicionar_palavra(matriz, "MOUSE", "horizontal", 9, 8)
    adicionar_palavra(matriz, "MONITOR", "vertical", 10, 18)
    adicionar_palavra(matriz, "GABINETE", "horizontal", 14, 2)
    adicionar_palavra(matriz, "COOLER", "vertical", 15, 22)
    adicionar_palavra(matriz, "BARRAMENTO", "horizontal", 18, 5)
    adicionar_palavra(matriz, "SLOT", "vertical", 20, 9)
    
# aqui o tema é escolhido aleatoriamente
def posicionar_palavras(matriz):
    variacoes = [jogo_verao_hardware]
    versao = choice(variacoes)
    versao(matriz)