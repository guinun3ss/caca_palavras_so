TAMANHO_GRADE = 25 # número de linhas e colunas da matriz
TAMANHO_CELULA = 25 # tamanho de cada letra em pixels

MARGEM = 20

LARGURA_JANELA = TAMANHO_GRADE * TAMANHO_CELULA + MARGEM * 2
ALTURA_JANELA = TAMANHO_GRADE * TAMANHO_CELULA + MARGEM * 2

# cores dos elementos visuais
COR_FUNDO = "white"
COR_CONTORNO = "gray"
COR_TEXTO = "black"

COR_SELECAO = "#ADD8E6" # cor que aparece na hora de selecionar uma palavra
COR_ACHADA = "#90EE90" # cor da palavra encontrada, fica permanente

LETRAS = ["A", "Á", "Â", "Ã", "À", "B", "C", "D", "E", "É",
          "Ê", "F", "G", "H", "I", "Í", "J", "K", "L", "M",
          "N", "O", "Ó", "Ô", "Õ", "P", "Q", "R", "S", "T",
          "U", "Ú", "V", "W", "X", "Y", "Z"]

PALAVRAS = {"HARDWARE", "MEMÓRIA", "BARRAMENTO",
            "MAINFRAME", "COMPUTADOR", "ENIAC",
            "VÁLVULA", "TRANSISTOR", "UNIX",
            "PROCESSADOR", "LINUX", "MULTIPROGRAMAÇÃO",
            "BINÁRIO", "GUI"}