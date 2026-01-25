TAMANHO_MATRIZ = 25 # define quantas letras a matriz vai ter
TAMANHO_CELULA = 25 # tamanho de cada célula em px

MARGEM = 20

# tamanho final da janela que o jogo vai ocupar
LARGURA_JANELA = TAMANHO_MATRIZ * TAMANHO_CELULA + MARGEM * 2
ALTURA_JANELA = TAMANHO_MATRIZ * TAMANHO_CELULA + MARGEM * 2

COR_FUNDO = "white"
COR_CONTORNO = "gray"
COR_TEXTO = "black"

COR_SELECAO = "#f5dd9d" # cor enquanto o mouse é pressionado
COR_ACHADA = "#c0d88c" # cor persistente se a palavra for correta

# as letras daqui são sorteadas para formar a matriz sem palavras
LETRAS = ["A", "Á", "Â", "Ã", "À", "B", "C", "D", "E", "É",
          "Ê", "F", "G", "H", "I", "Í", "J", "K", "L", "M",
          "N", "O", "Ó", "Ô", "Õ", "P", "Q", "R", "S", "T",
          "U", "Ú", "V", "W", "X", "Y", "Z"]