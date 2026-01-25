from random import choice # para sortear as letras da matriz
from configuracoes import TAMANHO_MATRIZ, LETRAS

def gerar_matriz():
    # cada linha da matriz é um list comprehension aleatório de LETRAS
    matriz = [[choice(LETRAS) for i in range(TAMANHO_MATRIZ)]
              for j in range(TAMANHO_MATRIZ)]
    return matriz

# aqui as palavras são posicionadas no meio das letras aleatórias
# é preciso calcular as posições e direções para evitar a sobreposição
def adicionar_palavra(matriz, palavra, direcao, linha, coluna):
    # a palavra é desmembrada
    # e cada letra dela substitui uma letra aleatória
    for i, letra in enumerate(palavra): # o i avança para a próxima linha/coluna
        if direcao == "horizontal":
            matriz[linha][coluna + i] = letra
        elif direcao == "vertical":
            matriz[linha + i][coluna] = letra

# cada uma dessas funções corresponde a uma fase do jogo
def jogo_versao_hardware(matriz):
    # e essa lista é para informar ao jogador as palavras que deve achar
    palavras_procuradas = ["PLACA", "FONTE", "MEMÓRIA", "PROCESSADOR",
                           "DISCO", "TECLADO", "MOUSE", "MONITOR", 
                           "GABINETE", "COOLER", "BARRAMENTO", "SLOT"]
    
    # aqui as palavras são posicionadas de fato
    # como mencionado, precisa calcular com precisão as posições
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

# mais uma fase
def jogo_versao_historia(matriz):
    palavras_procuradas = ["VÁLVULA", "ENIAC", "TRANSISTOR", "UNIX",
                           "MACINTOSH", "MAINFRAME", "ASSEMBLY", "MICROPROCESSADOR",
                           "APPLE", "FORTRAN", "WINDOWS", "GUI"]
    
    adicionar_palavra(matriz, "MICROPROCESSADOR", "horizontal", 2, 2)
    adicionar_palavra(matriz, "TRANSISTOR", "vertical", 1, 5)
    adicionar_palavra(matriz, "ASSEMBLY", "vertical", 0, 22)
    adicionar_palavra(matriz, "APPLE", "vertical", 4, 20)
    adicionar_palavra(matriz, "MACINTOSH", "horizontal", 12, 3)
    adicionar_palavra(matriz, "MAINFRAME", "vertical", 8, 18)
    adicionar_palavra(matriz, "ENIAC", "horizontal", 10, 16)
    adicionar_palavra(matriz, "FORTRAN", "horizontal", 15, 0)
    adicionar_palavra(matriz, "WINDOWS", "horizontal", 18, 15)
    adicionar_palavra(matriz, "UNIX", "vertical", 20, 2)
    adicionar_palavra(matriz, "GUI", "vertical", 21, 14)
    adicionar_palavra(matriz, "VÁLVULA", "horizontal", 22, 10)

    return palavras_procuradas

# outra fase
def jogo_versao_sistema(matriz):
    palavras_procuradas = ["TERMINAL", "EMBARCADO", "FIRMWARE", "INTERRUPÇÃO",
                           "THREAD", "DRIVER", "PROCESSO", "BUFFER",
                           "BOOT", "KERNEL", "BIOS", "ESCALONADOR"]
    
    adicionar_palavra(matriz, "TERMINAL", "horizontal", 0, 4)
    adicionar_palavra(matriz, "EMBARCADO", "vertical", 2, 20)
    adicionar_palavra(matriz, "FIRMWARE", "horizontal", 5, 2)
    adicionar_palavra(matriz, "INTERRUPÇÃO", "vertical", 7, 3)
    adicionar_palavra(matriz, "THREAD", "vertical", 8, 13)
    adicionar_palavra(matriz, "DRIVER", "horizontal", 10, 12)
    adicionar_palavra(matriz, "PROCESSO", "horizontal", 19, 5)
    adicionar_palavra(matriz, "BUFFER", "vertical", 15, 9)
    adicionar_palavra(matriz, "BOOT", "vertical", 16, 14)
    adicionar_palavra(matriz, "KERNEL", "horizontal", 18, 18)
    adicionar_palavra(matriz, "BIOS", "horizontal", 20, 2)
    adicionar_palavra(matriz, "ESCALONADOR", "horizontal", 22, 5)

    return palavras_procuradas

# fase final
def jogo_versao_linguagens(matriz):
    palavras_procuradas = ["PYTHON", "JAVA", "LUA", "TYPESCRIPT",
                           "COBOL", "PHP", "SWIFT", "KOTLIN", 
                           "RUST", "RUBY", "ASSEMBLY", "FORTRAN"]
    
    adicionar_palavra(matriz, "COBOL", "vertical", 0, 18)
    adicionar_palavra(matriz, "TYPESCRIPT", "horizontal", 2, 2)
    adicionar_palavra(matriz, "ASSEMBLY", "vertical", 5, 15) 
    adicionar_palavra(matriz, "RUBY", "vertical", 5, 20)
    adicionar_palavra(matriz, "RUST", "horizontal", 6, 13)
    adicionar_palavra(matriz, "LUA", "horizontal", 8, 7)
    adicionar_palavra(matriz, "PYTHON", "vertical", 8, 3)
    adicionar_palavra(matriz, "JAVA", "vertical", 14, 10)
    adicionar_palavra(matriz, "FORTRAN", "horizontal", 15, 5)
    adicionar_palavra(matriz, "PHP", "horizontal", 15, 19)
    adicionar_palavra(matriz, "KOTLIN", "horizontal", 18, 15)
    adicionar_palavra(matriz, "SWIFT", "horizontal", 22, 2)

    return palavras_procuradas

# essa lista vai ser usada para avançar as fases
FASES = [jogo_versao_hardware, jogo_versao_historia,
         jogo_versao_sistema, jogo_versao_linguagens]