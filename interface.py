import tkinter as tk # para a interface gráfica
from tkinter import messagebox # para exibir mensagens ao usuário
from configuracoes import *
from jogo import gerar_matriz, FASES

class Jogo:
    def __init__(self, janela):
        self.janela = janela # para inicializar a janela do jogo

        self.fases = FASES
        self.indice_fase = 0 # esse índice vai ser incrementado em 1 a cada fase
        self.contador_palavras_encontradas = 0 # conta as palavras encontradas

        # divide a tela entre a matriz e a lista de palavras
        frame_principal = tk.Frame(janela)
        frame_principal.pack()

        # personalização do frame principal
        # também vai auxiliar na manipulação dos eventos do mouse
        self.canvas = tk.Canvas(frame_principal, width=LARGURA_JANELA,
                                height=ALTURA_JANELA, bg=COR_FUNDO)
        self.canvas.pack(side="left") # e o pack coloca tudo na janela

        # aqui são posicionadas as palavras que o jogador deve encontrar
        self.palavras_exibidas = tk.Text(frame_principal, wrap="word",
                                        font=("Arial", 11), width=25,
                                        height=15, relief="flat")
        self.palavras_exibidas.pack(side="right", padx=10)
        self.palavras_exibidas.config(state="disabled")

        self.celulas_destacadas = {} # células com palavras do jogo, persistente
        self.celulas_selecionadas = [] # palavras selecionadas temporariamente
        self.selecionada = False # só é verdadeira quando o botão do mouse estiver pressionado

        # coordenadas das células selecionadas
        self.inicio = None
        self.fim = None

        # e aqui são manipulados os eventos do mouse de fato
        self.canvas.bind("<ButtonPress-1>", self.clique_mouse) # quando pressiona o botão
        self.canvas.bind("<B1-Motion>", self.movimento_mouse) # quando movimenta o ponteiro
        self.canvas.bind("<ButtonRelease-1>", self.soltar_botao_mouse) # quando solta o botão

        self.iniciar_fase()

    # inicia uma fase com tudo zerado
    def iniciar_fase(self):
        self.celulas_destacadas = {}
        self.celulas_selecionadas = []
        self.contador_palavras_encontradas = 0
        
        self.matriz = gerar_matriz()

        # a próxima fase é chamada quando o índice é incrementado
        fase_atual = self.fases[self.indice_fase]

        # e aqui é garantido que só as palavras da fase sejam exibidas
        self.lista_palavras = fase_atual(self.matriz)

        # a interface é atualiizada para a fase seguinte
        self.palavras_exibidas.config(state="normal")
        self.palavras_exibidas.delete("1.0", "end")
        for p in self.lista_palavras:
            self.palavras_exibidas.insert("end", p + "\n")
        self.palavras_exibidas.config(state="disabled")

        # título da janela contendo a fase atual do jogo
        self.janela.title(f"Fase {self.indice_fase + 1} de {len(self.fases)}")

        self.desenhar()

    def desenhar(self): # renderização do estado atual do jogo
        self.canvas.delete("all")
        # um quadrado é desenhado na grade para cada célula
        for l in range(TAMANHO_MATRIZ):
            for c in range(TAMANHO_MATRIZ):
                self.desenhar_celula(l, c, None)

        # aqui as palavras corretas são destacadas e sobrescritas
        for(l,c), cor in self.celulas_destacadas.items():
            self.desenhar_celula(l, c, cor)
            
        # aqui as células selecionadas são destacadas temporariamente
        # depois a seleção é apagada, se não estiver na lista de palavras
        for l, c in self.celulas_selecionadas:
            self.desenhar_celula(l, c, COR_SELECAO)

    # desenhar o contorno da célula
    def desenhar_celula(self, linha, coluna, preenchimento):
        x1 = MARGEM + coluna * TAMANHO_CELULA
        y1 = MARGEM + linha * TAMANHO_CELULA
        x2 = x1 + TAMANHO_CELULA
        y2 = y1 + TAMANHO_CELULA

        # desenha os espaços para cada letra da matriz
        self.canvas.create_rectangle(x1, y1, x2, y2,
                                     outline=COR_CONTORNO,
                                     fill=preenchimento if preenchimento else "")
            
        # e formata o texto que vai aparecer na matriz
        self.canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2,
                                text=self.matriz[linha][coluna],
                                fill=COR_TEXTO, font=("Arial", 12, "bold"))
            
    # métodos de seleção das palavras
    def posicao_para_celula(self, x, y):
        coluna = (x - MARGEM) // TAMANHO_CELULA
        linha = (y - MARGEM) // TAMANHO_CELULA

        # garantir que o clique não vai ultrapassar a matriz
        if 0 <= linha < TAMANHO_MATRIZ and 0 <= coluna < TAMANHO_MATRIZ:
            return linha, coluna
        return None
        
    def atualizar_selecao(self):
        # remover a seleção anterior
        self.celulas_selecionadas.clear()

        li, ci = self.inicio
        lf, cf = self.fim

        # atualiza a seleção de acordo com a direção
        # horizontal e vertical
        if li == lf:
            passo = 1 if ci <= cf else -1
            for c in range(ci, cf + passo, passo):
                    self.celulas_selecionadas.append((li, c))
        elif ci == cf:
            passo = 1 if li <= lf else -1
            for l in range(li, lf + passo, passo):
                self.celulas_selecionadas.append((l, ci))

    # manipulação dos eventos do mouse
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

        # transforma as células selecionadas em uma string única
        palavra = "".join(self.matriz[l][c] for l, c in self.celulas_selecionadas)

        # e verifica se a seleção forma alguma palavra que está no jogo
        # o fatiamento de string é para permitir seleções ao contrário também
        if palavra in self.lista_palavras or palavra[::-1] in self.lista_palavras:
            for c in self.celulas_selecionadas:
                # destacar a palavra encontrada permanentemente
                # se a palavra existir na lista
                self.celulas_destacadas[c] = COR_ACHADA
            
            palavra_correta = palavra if palavra in self.lista_palavras else palavra[::-1]
            self.atualizar_lista_palavras(palavra_correta)

        # limpar as células selecionadas
        # só as que tem palavras persistem
        self.celulas_selecionadas.clear()
        self.desenhar() # ataualizar a tela

    # pinta de verde as palavras que já foram encontradas
    def atualizar_lista_palavras(self, palavra_encontrda):
        self.palavras_exibidas.config(state="normal")
        
        start = "1.0"
        pos = self.palavras_exibidas.search(palavra_encontrda, start, stopindex="end")
        if pos:
            tags = self.palavras_exibidas.tag_names(pos)
            if "encontrada" not in tags:
                end = f"{pos} + {len(palavra_encontrda)}c"
                self.palavras_exibidas.tag_add("encontrada", pos, end)
                self.palavras_exibidas.tag_config("encontrada", foreground="green",
                                                font=("Arial", 12, "bold"))
                
                # e incrementa as palavras encontradas
                # ajuda na mudança das fase
                self.contador_palavras_encontradas += 1

                # lógica para avançar de fase
                # só avança se o contador for igual ao tamanho da lista
                if self.contador_palavras_encontradas == len(self.lista_palavras):
                    self.indice_fase += 1
                    if self.indice_fase < len(self.fases):
                        messagebox.showinfo("Parabéns!", "Fase concluída! Vamos para a próxima!")
                        self.iniciar_fase() # o jogador avança de fato aqui
                    else:
                        messagebox.showinfo("Parabéns!", "Você completou todas as fases!")
                        self.janela.quit() # se não tiver mais fases, o jogo cai aqui e encerra
            
            # atualiza o estado das palavras que ficam do lado da matriz
            self.palavras_exibidas.config(state="disabled")