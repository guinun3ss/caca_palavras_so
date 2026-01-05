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

# a posição deve ser calculada para evitar a sobreposição das palavras
def posicionar_palavras(matriz):
    adicionar_palavra(matriz, "HARDWARE", "horizontal", 0, 0)
    adicionar_palavra(matriz, "MEMÓRIA", "vertical", 14, 10)
    adicionar_palavra(matriz, "BARRAMENTO", "horizontal", 2, 12)
    adicionar_palavra(matriz, "MAINFRAME", "vertical", 9, 23)
    adicionar_palavra(matriz, "COMPUTADOR", "horizontal", 11, 4)
    adicionar_palavra(matriz, "ENIAC", "horizontal", 12, 15)
    adicionar_palavra(matriz, "VÁLVULA", "vertical", 13, 5)
    adicionar_palavra(matriz, "TRANSISTOR", "vertical", 14, 18)
    adicionar_palavra(matriz, "UNIX", "vertical", 19, 3)
    adicionar_palavra(matriz, "PROCESSADOR", "horizontal", 3, 0)
    adicionar_palavra(matriz, "LINUX", "horizontal", 4, 13)
    adicionar_palavra(matriz, "MULTIPROGRAMAÇÃO", "horizontal", 6, 2)
    adicionar_palavra(matriz, "BINÁRIO", "horizontal", 24, 4)
    adicionar_palavra(matriz, "GUI", "horizontal", 9, 8)