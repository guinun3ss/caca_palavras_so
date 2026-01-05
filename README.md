# caca_palavras_so
Repositório referente ao jogo de caça-palavras solicitado na discipilina de Sistemas Operacionais.

## Para a implementação da interface gráfica do jogo, foi utilizada a biblioteca **tkinker**.

# Informações sobre os módulos do jogo
## configuracoes.py
Módulo referente às configurações globais do jogo. Neste módulo estão guardadas constantes que armazenam informações importantes para o funcionamento do jogo como um todo, como as palavras a serem procuradas e configurações da interface gráfica, como dimensões e cores.

## jogo.py
Módulo referente à lógica do jogo em si. Este módulo contém todas as funções relacionadas a como o jogo funciona, como a geração da matriz que vai guardas as palavras, adição de palavras na matriz e verificação do tamanho das palavras, para saber se cabem na matriz.

## interface.py
O módulo interface contém todas as configurações da interface gráfica especificamente e como mencionado anteriormente, a interface foi implementada utilizando a biblioteca **tkinter**.

## main.py
Onde todos os módulos se encontram para poder executar o jogo.