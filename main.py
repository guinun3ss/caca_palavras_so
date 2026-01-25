import tkinter as tk
from interface import Jogo

if __name__ == "__main__":
    janela = tk.Tk()
    Jogo(janela) # por fim, a janela é inicializda junto com a classe da interface
    janela.mainloop() # e o mainloop mantém a janela ativa