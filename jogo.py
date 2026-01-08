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
def jogo_versao_hardware(matriz):
    palavras_procuradas = {"PLACA", "FONTE", "MEMÓRIA", "PROCESSADOR",
                           "DISCO", "TECLADO", "MOUSE", "MONITOR", 
                           "GABINETE", "COOLER", "BARRAMENTO", "SLOT"}
    
    adicionar_palavra(matriz, "PLACA", "vertical", 20, 20)
    adicionar_palavra(matriz, "FONTE", "vertical", 1, 4)
    adicionar_palavra(matriz, "MEMÓRIA", "horizontal", 15, 10)
    adicionar_palavra(matriz, "PROCESSADOR", "horizontal", 2, 2)
    adicionar_palavra(matriz, "DISCO", "horizontal", 23, 12)
    adicionar_palavra(matriz, "TECLADO", "vertical", 0, 15)
    adicionar_palavra(matriz, "MOUSE", "vertical", 12, 2)
    adicionar_palavra(matriz, "MONITOR", "horizontal", 20, 3)
    adicionar_palavra(matriz, "GABINETE", "horizontal", 10, 5)
    adicionar_palavra(matriz, "COOLER", "horizontal", 10, 16)
    adicionar_palavra(matriz, "BARRAMENTO", "vertical", 4, 20)
    adicionar_palavra(matriz, "SLOT", "horizontal", 13, 0)

    return palavras_procuradas
    
# aqui o tema é escolhido aleatoriamente
def posicionar_palavras(matriz):
    variacoes = [jogo_versao_hardware]
    versao = choice(variacoes)
    return versao(matriz)