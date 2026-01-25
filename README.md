# caca_palavras_so
Repositório referente ao jogo de caça-palavras solicitado para a discipilina de Sistemas Operacionais, do Professor Warlles Machado.

## Para a implementação da interface gráfica do jogo, foi utilizada a biblioteca padrão do Python, **tkinker**.

# Informações sobre os módulos do jogo
## configuracoes.py
O módulo **configuracoes.py** refere-se às configurações globais do jogo. Nele estão todas as constantes que são usadas para a cosntrução dos demais módulos do jogo, como o tamanho da janela do jogo, a lista de letras da matriz, entre outras variáveis necessárias.

## jogo.py
**jogo.py** refere-se à lógica do jogo em si. Nele estão todas as funções referentes à construção pura do jogo, como a função que gera a matriz de letras aleatórias, a função que adiciona palavra à matriz, além das fases do jogo e outras funções.

## interface.py
O módulo **interface.py** centraliza toda a implementação dos elementos gráficos do jogo por meio de uma classe. Tudo o que se refere às configurações diretas da interface está no módulo, exceto algumas constantes globais, que foram mantidas em **configuracoes.py**.

## main.py
No módulo **main.py**, a classe Jogo é inicializda juntamente com a janela do jogo.