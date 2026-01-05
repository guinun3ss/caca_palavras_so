import tkinter as tk
from configuracoes import *
from jogo import gerar_matriz, posicionar_palavras

class Jogo:
    def __init__(self, janela):
        self.janela = janela
        # nome que aparece parte superior da janela
        self.janela.title("Caça-Palavras Temático")

        # para manipular os movimentos do mouse
        self.canvas = tk.Canvas(janela, width=LARGURA_JANELA,
                                height=ALTURA_JANELA, bg=COR_FUNDO)
        self.canvas.pack() # adiciona o canvas à janela

        self.matriz = gerar_matriz()
        posicionar_palavras(self.matriz)

        # guarda as células com as palavras selecionadas corretamente
        self.celulas_destacadas = {}

        # guardar as células selecionadas temporariamente
        self.celulas_selecionadas = []
        self.selecionada = False # só é True quando pressiona o botão do mouse

        # coordendas da célula selecionada
        self.inicio = None
        self.fim = None

        # manipulação dos eventos do mouse
        self.canvas.bind("<ButtonPress-1>", self.mouse_down)
        self.canvas.bind("<B1-Motion>", self.mouse_move)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_up)

        self.desenhar()

        # métodos de desenho da tela
    def desenhar(self):
        self.canvas.delete("all")

        # desenho das células vazias
        for l in range(TAMANHO_GRADE):
            for c in range(TAMANHO_GRADE):
                self.desenhar_celula(l, c, None)

        # destacar palavras encontradas
        for(l,c), cor in self.celulas_destacadas.items():
            self.desenhar_celula(l, c, cor)
            
        # destacar temporariamente as células selecionadas
        for l, c in self.celulas_selecionadas:
            self.desenhar_celula(l, c, COR_SELECAO)

    # desenhar o contorno da célula
    def desenhar_celula(self, linha, coluna, fill):
        x1 = MARGEM + coluna * TAMANHO_CELULA
        y1 = MARGEM + linha * TAMANHO_CELULA
        x2 = x1 + TAMANHO_CELULA
        y2 = y1 + TAMANHO_CELULA

        self.canvas.create_rectangle(x1, y1, x2, y2,
                                     outline=COR_CONTORNO,
                                     fill=fill if fill else "")
            
        # formatação do texto da grade
        self.canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2,
                                text=self.matriz[linha][coluna],
                                fill=COR_TEXTO, font=("Arial", 12, "bold"))
            
        # métodos de seleção das palavras
    def posicao_para_celula(self, x, y):
        coluna = (x - MARGEM) // TAMANHO_CELULA
        linha = (y - MARGEM) // TAMANHO_CELULA

        #garantir que o clique está na grade
        if 0 <= linha < TAMANHO_GRADE and 0 <= coluna < TAMANHO_GRADE:
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
                self.celulas_selecionadas.append(l, ci)

        # eventos do mouse
    def mouse_down(self, event): # iniciar a seleção e marcar o ponto inicial
        celula = self.posicao_para_celula(event.x, event.y)
                
        if celula:
            self.selecionada = True
            self.inicio = self.fim = celula
            self.celulas_selecionadas.clear()
            self.desenhar()

    def mouse_move(self, event):
        if not self.selecionada:
            return # encerra aqui se não tiver nada selecionado
                
        celula = self.posicao_para_celula(event.x, event.y)
                
        if celula:
            self.fim = celula
            self.atualizar_selecao()
            self.desenhar()

    def mouse_up(self, event):
        self.selecionada = False
        palavra = "".join(self.matriz[l][c] for l, c in self.celulas_selecionadas)

        if palavra in PALAVRAS:
            for c in self.celulas_selecionadas:
                # destacar a palavra encontrada permanentemente
                self.celulas_destacadas[c] = COR_ACHADA
            print("Correto: ", palavra)

            # limpar as células selecionadas
            self.celulas_selecionadas.clear()
            self.desenhar() # ataualizar a tela