import tkinter as tk
from configuracoes import *
from jogo import gerar_matriz, posicionar_palavras

class Jogo:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Caça-Palavras Temático")

        # dividir a tela entre a matriz e o texto
        frame_principal = tk.Frame(janela)
        frame_principal.pack()
        
        # o Canvas ajuda na manipulação dos movimentos do mouse
        self.canvas = tk.Canvas(frame_principal, width=LARGURA_JANELA,
                                height=ALTURA_JANELA, bg=COR_FUNDO)
        self.canvas.pack(side="left") # e o pack coloca tudo na janela

        self.matriz = gerar_matriz()
        self.lista_palavras = posicionar_palavras(self.matriz)

        # exibir palavras a serem encontradas no jogo
        palavras_jogo = "\n".join(self.lista_palavras)
        self.palavras_exibidas = tk.Text(frame_principal, wrap="word",
                                        font=("Arial", 11), width=25,
                                        height=len(self.lista_palavras) + 2,
                                        relief="flat")
        self.palavras_exibidas.pack(side="right", padx=10)

        for palavra in self.lista_palavras:
            self.palavras_exibidas.insert("end", palavra + "\n")

        self.palavras_exibidas.config(state="disabled")

        self.celulas_destacadas = {} # palavras selecionadas corretamente
        self.celulas_selecionadas = [] # palavras selecionadas temporariamente
        self.selecionada = False # só é True quando o o botão do mouse é pressionado

        # coordenadas das células selecionadas
        self.inicio = None
        self.fim = None

        # aqui são manipuladas as açoes feitas com o mouse
        self.canvas.bind("<ButtonPress-1>", self.clique_mouse) # quando o botão é pressionado
        self.canvas.bind("<B1-Motion>", self.movimento_mouse) # quando o ponteiro é movido
        self.canvas.bind("<ButtonRelease-1>", self.soltar_botao_mouse) # quando o botão é solto

        self.desenhar()

    def desenhar(self): # renderização do estado atual do jogo
        self.canvas.delete("all")

        # desenhar os números fora da grade
        # NÃO FAZ PARTE DO JOGO, APAGAR DEPOIS
        for c in range(TAMANHO_MATRIZ):
            x = MARGEM + c * TAMANHO_CELULA + TAMANHO_CELULA // 2
            y = MARGEM // 2   # posição acima da grade
            self.canvas.create_text(x, y, text=str(c), font=("Arial", 10, "bold"), fill="black")

        for l in range(TAMANHO_MATRIZ):
            x = MARGEM // 2   # posição à esquerda da grade
            y = MARGEM + l * TAMANHO_CELULA + TAMANHO_CELULA // 2
            self.canvas.create_text(x, y, text=str(l), font=("Arial", 10, "bold"), fill="black")

        for l in range(TAMANHO_MATRIZ):
            x = MARGEM // 2
            y = MARGEM + l * TAMANHO_CELULA + TAMANHO_CELULA // 2

            self.canvas.create_text(x, y, text=str(l),
                                     font=("Arial", 10, "bold"),
                                     fill="black")

        # um quadrado é desenhado na grade para cada célula
        for l in range(TAMANHO_MATRIZ):
            for c in range(TAMANHO_MATRIZ):
                self.desenhar_celula(l, c, None)

        # aqui as palavras corretas são destacadas e sobrescritas
        for(l,c), cor in self.celulas_destacadas.items():
            self.desenhar_celula(l, c, cor)
            
        # aqui as células selecionadas são destacadas temporariamente
        for l, c in self.celulas_selecionadas:
            self.desenhar_celula(l, c, COR_SELECAO)

    # desenhar o contorno da célula
    def desenhar_celula(self, linha, coluna, preenchimento):
        x1 = MARGEM + coluna * TAMANHO_CELULA
        y1 = MARGEM + linha * TAMANHO_CELULA
        x2 = x1 + TAMANHO_CELULA
        y2 = y1 + TAMANHO_CELULA

        self.canvas.create_rectangle(x1, y1, x2, y2,
                                     outline=COR_CONTORNO,
                                     fill=preenchimento if preenchimento else "")
            
        # formatação do texto da MATRTAMANHO_MATRIZ
        self.canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2,
                                text=self.matriz[linha][coluna],
                                fill=COR_TEXTO, font=("Arial", 12, "bold"))
            
        # métodos de seleção das palavras
    def posicao_para_celula(self, x, y):
        coluna = (x - MARGEM) // TAMANHO_CELULA
        linha = (y - MARGEM) // TAMANHO_CELULA

        #garantir que o clique está na MATRTAMANHO_MATRIZ
        if 0 <= linha < TAMANHO_MATRIZ and 0 <= coluna < TAMANHO_MATRIZ:
            return linha, coluna
        return None
        
    def atualizar_selecao(self):
        # remover a seleção anterior
        self.celulas_selecionadas.clear()
        li, ci = self.inicio
        lf, cf = self.fim

        if li == lf:
            passo = 1 if ci <= cf else -1
            for c in range(ci, cf + passo, passo):
                    self.celulas_selecionadas.append((li, c))
        elif ci == cf:
            passo = 1 if li <= lf else -1
            for l in range(li, lf + passo, passo):
                self.celulas_selecionadas.append((l, ci))

        # eventos do mouse
    def clique_mouse(self, event): # iniciar a seleção e marcar o ponto inicial
        celula = self.posicao_para_celula(event.x, event.y)
                
        if celula:
            self.selecionada = True
            self.inicio = self.fim = celula
            self.celulas_selecionadas.clear()
            self.desenhar()

    def movimento_mouse(self, event):
        if not self.selecionada:
            return # encerra aqui se não tiver nada selecionado
                
        celula = self.posicao_para_celula(event.x, event.y)
                
        if celula:
            self.fim = celula
            self.atualizar_selecao()
            self.desenhar()

    def soltar_botao_mouse(self, event):
        self.selecionada = False

        palavra = "".join(self.matriz[l][c] for l, c in self.celulas_selecionadas)

        if palavra in PALAVRAS or palavra[::-1] in PALAVRAS:
            for c in self.celulas_selecionadas:
                # destacar a palavra encontrada permanentemente
                self.celulas_destacadas[c] = COR_ACHADA

            # limpar as células selecionadas
        self.celulas_selecionadas.clear()
        self.desenhar() # ataualizar a tela

        self.atualizar_lista_palavras(palavra if palavra in self.lista_palavras else palavra[::-1])

    # excluir palavras que já foram encontradas
    def atualizar_lista_palavras(self, palavra_encontrda):
        self.palavras_exibidas.config(state="normal")
        
        start = "1.0"
        pos = self.palavras_exibidas.search(palavra_encontrda, start, stopindex="end")
        if pos:
            end = f"{pos} + {len(palavra_encontrda)}c"
            self.palavras_exibidas.tag_add("encontrada", pos, end)
            self.palavras_exibidas.tag_config("encontrada", foreground="green",
                                              font=("Arial", 12, "bold"))
            
            self.palavras_exibidas.config(state="disabled")