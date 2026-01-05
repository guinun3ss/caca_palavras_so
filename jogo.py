from random import choice
from configuracoes import TAMANHO_GRADE, LETRAS

def gerar_matriz():
    # cada linha é uma seleção aleatória de LETRAS do módulo configuracoes
    matriz = [[choice(LETRAS) for i in range(TAMANHO_GRADE)]
              for j in range(TAMANHO_GRADE)]
    return matriz

# retorna um booleano a partir da comparação da palavra
# com o lugar que ela vai ficar na matriz
def cabe_na_matriz(palavra, direcao, linha, coluna):
    if direcao == "horizontal":
        return coluna + len(palavra) <= TAMANHO_GRADE
    if direcao == "vertical":
        return linha + len(palavra) <= TAMANHO_GRADE
    return False

def adicionar_palavra(matriz, palavra, direcao, linha, coluna):
    if not cabe_na_matriz(palavra, direcao, linha, coluna):
        return # se não couber na matriz, a função encerra aqui
    
    for i, letra in enumerate(palavra):
        if direcao == "horizontal": # aqui as colunas são percorridas
            matriz[linha][coluna + i] = letra
        elif direcao == "vertical": # aqui as linhas são percorridas
            matriz[linha + i][coluna] = letra

# aqui é só para fazer as chamadas de adicionar_palavra
# é só uma questão de organização, para facilitar a manutenção
def posicionar_palavras(matriz):
    # as palavras não podem se cruzar porque suas letras vão se sobrepor
    # a posição de cada uma deve ser calculada para evitar esse problema
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