# CURSO DE PYTHON

*"Na maneira Python de pensar, explícito é melhor do que implícito e simples é melhor do que complexo."*

### O QUE É PYTHON?

Se você está lendo isso, talvez já tenha uma idéia do que seja PYTHON e porque é importante conhecer essa ferramenta.
Mas antes de mais nada, vou apresentar algumas das razões da popularidade do Python.

PRA QUE SERVE PYTHON

ONDE É UTILIZADO PYTHON

PORQUE AS PESSOAS USAM PYTHON

Como hoje existem muitas linguagens de programação essa normalmente é a primeira pergunta dos novatos.
Dadas as ventenas de milhares de usuários de Python hoje existentes, na verdade não há como responder essa pergunta com total precisão. 
A escolha das ferramentas de desenvolvimento é às vezes baseada em limitações específicas ou na preferência pessoal. (" Aprendendo Python by.... pegar o nome do cara)

### "Qualidade de software"
Python da legibilidade coerência e qualidade do software em geral.
O código em Python é projetado para ser legível e, portanto fácil de manter.
Além disso, o Python tem excelente suporte para mecanismo de reutilização de código, como a programação orientada a objeto (POO)
### "Produtividade do desenvolvedor"
O Python aumenta a produtividade do desenvolvedor, Python normalmente tem de 1/3 a 1/5 do tamanho do código equivalente em C++ ou Java.
Isso signigica menos dgitação, menos depuração e menos manutenção após o desenvolvimento.
### "Portabilidade do programa"
Portar um código Python entre o Unix e o Windows, por exemplo, normalmente é apenas uma questão de copiar o código entre as máquinas.
### "Bibliotecas de suporte"
O Python vem com um grande conjunto de funcionalidades pré-compiladas e portáveis, conhecidas como bibliotecas padrão.
As bibliotecas suportam diversas tarefas de programação em nível de aplicativo, desde text pattern matching, até scripts de rede.
### "Integração de componentes"
Os scripts em Python podem se comunicar facilmente com outras partes de um aplicativo, usando uma variedade de mecanismo de integração e extenção de produto.
Atualmente, o código Python pode chamar bibiotecas C e C++, pode ser chamado a partir de programas em C e C++, pode ser integrado com componentes Java, pode ser comunicar por meio de .COM e .NET e pode interagir pela rede, com interfaces como SOAP e XML-RPC.


## O QUE EU POSSO FAZER COM PYTHON?

Além de ser uma linguagem de programação bem projetada, o python também é útil para executar tarefas do mundo real - os tipos de coisas que os desenvolvedires fazem todo dia. Ele é coumente usado em diversos domínios, como ferramenta para escrever outros componentes e implementar programas independentes. Na verdade, como linguagem de propósito geral, as funções do Python são praticamente ilimitadas.
Entretanto, as funcções mais comunds do Puthon parecem recair em algumas caregorias mais amplas. As próximas seções descrevem algumas das applicações mais comuns do Python, assim como as ferramentas usadas em cada domínio. Não podemos descrever todas as ferramentas mencionadas aqui; se você estiver interessado em algum desses asssuntos , veja o Python on-line ou outros recursos, para obter mais detalhes.


# PROGRAMAÇÃO DE SISTEMAS


As interfaces incorporadas do Python para serviçoes de sistemas operacional o tornam ideal para escrever ferramentas e utilitários de administração de sistemas portáveis e fáceis de manter(às vezes chamadas de ferramentas de shel). Os programas em Python podem pesquisar arquivos e árvores de diretório, camar outros programas, realizar processamento paralelo com processos e segmentos etc.

A biblioteca padrão do Python vem com vínculos POSIX e suporte para todas as ferrametnas de sistemas operacional comuns: variáveis de ambiente, arquivos, sockets, pipes, processos, múltiplos sefmentos, expressôes regulares para correspondência de padrão de texto, argumentos de linha de comandos, interfaces de fluxo padão, execução de comando de shell, expansão de nome de arquivo e muito mias. Além disso, a maior parte das interfaces de sitema do Python é projetada para ser portável: por exemplo, um script que copia a´rvores de diretório normalmente é exeutado sem alterção em todas as principais plataformas Python.


# GUIs

A simplicidade e o rápido retorno do Python também o tornam bom para programação de GUI(Interface gráfica com o usuário).
O python vem com uma interface orientada a objetos padrão para a API de GUI Tk, chamada Tkinter, que permite aos programas em Python implementarem GUIs portáveis com aparência e comportamento nativos. As GUIs Python/Tkinter são executadas sem alterações  no MS Windows, X Windows(no Unix e no Linux) e em Macs, Um pacote de extesões gratuito.

# SCRIPTS DE INTERNET

O Python vem com módulos para Internet padrão que permitem aos programas executar uma grande variedade de tarefas em rede, tanto no modo cliente como servidor. Os scripts podem comunicar-se por meio de sockets: extrair informações de formulários enviados para um script CGI no lado do servidor: transferir arquivos por meio de FTP: processar arquivos XML: enviar, receber e analisar email: niscar páginas da Web por meio de URLs: analisar o código HTML e XML das páginas buscadas da Web: comunicar-se por meio de XML-RPC, SOAP e telnet: e muito mais. As bibliotecas Pythjon tornam essas tarefas notavelmente simples.


# COMPOSIÇÃO RÁPIDA DE PROTÓTIPOS

Para os programs em Python, os componentes escritos em Python e C parecem iguais, por isso, é possível fazer o protótipo de sistemas inicialmente em Python e, então, mover componentes para uma linguagem compilada, como C ou C++, para distribuição. Ao contrário de algumas ferramentas de produção de protótipos, o Python não exige uma reescrita completa.


# PRIMEIROS PASSOS

CRIANDO HAMBIENTE DE TRABALHO

WINDOWS
CONSTRUINDO O AMBIENTE DE TRABALHO
Para começarmos a trabalhar e certificarmos que não teremos nenhum erro vamos se certificar que não tenha nenhuma versão do Python instalada.
Então a primeira coisa que iremos fazer é desistalar qualquer versão do python que esteja instalado em nosso computador.

Vamos em iniciar, digitamos painel de controle


CERTIFIQUE-SE DE QUE NÃO TENHA NENHUMA VERSÃO DO PYTHON instalada, até porque a melhor forma de gerenciar as versões do python é com a biblioteca anaconda.


INSTALANDO ANACONDA

Vamos abrir o navegador
vamos pesquisar anaconda no google
vamos abrir o site anaconda = https://www.anaconda.com/
vamos efetuar o download da biblioteca conda = https://www.anaconda.com/products/individual/download-success-2

feito isso vamos instalar a biblioteca
após instalado podemos ir agora no prompt de comando e ver se o python esta intalado

agora criaremos dois ambientes virtuais, para podermos gerenciar as duas versões do python
a 2.7 e a 3.0 endiante 

ainda no terminal vamos digitar

conda create --name python3 python=3.8

após a criação do ambiente virtual, vamos verificar se o mesmo foi criado com sucesso

conda env list

aqui vemos que foi criado o primeiro ambiente virtual e então teremos o ambiente python3 e o ambiente root ou base como preferir.
aqui como podemos ver estamos no ambiente base(root) o asteristico nos indica em qual ambiente estamos trabalhando atualmente

para alternamos de ambiente temos que digitar

activate (nome do ambiente virtual)
ex: 
activate python3

Para sairmos do ambiente virtual devemos digitar
deactivate (nome do ambiente virtual)
ou apenas deactivate


agora vamos criar um segundo ambiente virtual

vamos digitar conta create --name python2 python=2.7

agora vamos ter certeza que o abiente foi criado
pra isso vamos digitar
conda env list

como podemos ver, agora temos 3 ambientes virtuais

base = ambiente root
python2 = ambiente com o python 2.7
python3 = ambiente com o python 3.0 em diante

INSTALAÇÃO DA BIBLIOTECA KIVY NO AMBIENTE WINDOWS

mas antes disso temos que entender como está estruturado nosso ambiente de virtualização, para que possamos instalar a biblioteca kivy em ambas ou qualquer outra biblioteca sem erro algum...

aqui na lista de nomes temos a lista de nome dos dois ambientes que criamos e mais o ambiente root onde esta a instalação da conda( ou a instalação do python) você deve considerar que a instalação do projeto conda é em si a instalação do python, até porque o mesmo tem todos os arquivos necessários para rodar qualquer arquivo python, porém quando instalamos o projeto conda, não instalamos só os arquivos necessários para rodar o python, instalamos também diversas bbliotecas e também o script que nos permite trabalhar com ambientes virtuaisa pasta do projeto anaconda é uma instalação do python como qualquer outra porém é uma instalação do python que contem outros pacotes para as mais diversas tarefas

em seguida temos sempre que notar onde está o * o asteristico nos indica qual ambiente virtual esta ativo.
nesse caso estamos trabalhando no ambiente virtual root, ou seja na propria isntalação do conda

agora como podemos ver, estamos trabalhando no ambiente python3, como podemos ver o nome antes do PATH e o asteristico e também toda vez que um ambiente virtual que não for o root estiver ativo, vira na frente do path
e isso aocntece em qualquer sistema operacional, seja windows, linux ou mac,  o nome do ambiente virtual irá preceder o perfil do PATH do prompt de comando, agora podemos observar que todos os os ambientes estão armazenados no mesmo diretórios, porem cada ambiente virtual esta isolado em uma pasta
como foi dito antes, um ambiente virtual é uma instalação do python propriamente dita, nós temos que a pasta python3 e a pasta python2 e a pasta anaconda é uma instalação do pyhton também. quando alternamos um ambiente virtual, nós alternamos as configurações do prompt de comando






======

AGORA vamos no site da biblioteca kivy https://kivy.org/#home

https://kivy.org/doc/stable/gettingstarted/installation.html


vamos instalar o primeiramente o kivy no ambiente do python2


vamos digitar activate python2

temos que ter em mente, que toda vez que estramos no prompt temos que dizier em qual ambiente virtual queremos trabalhar.

caso contrário estaremos usando o python diretamente do projeto anaconda, o que geralmente não é recomendado

como podemos ver o nome do mesmo está precedendo o PATH

agora vamos aqui no site do kivy install
https://kivy.org/doc/stable/gettingstarted/installation.html#install-pip

e seguideremos o passo a passo para continuarmos a intalação

pip install --upgrade pip setuptools virtualenv

pip install docutils pygments pypiwin32 
pip install kivy.deps.sdl2
pip install kivy.deps.glew
pip install kivy.deps.gstreamer --extra-index-url https://kivy.org/downloads/packages/simple/
pip install kivy


podemos também intalar o kivy de outras maneiras

INSTALANDO PYCHARM
CRIANDO PROJETO


					PRIMEIROS COMANDDOS

VARIAVÉIS
PRINTS
INPUT

					NOTE






========================================================================================================================================================================================


A função print()







O If serve para verificar uma condição e o elif serve para verificar outra condição caso a condição do If seja falsa. No código não há muita diferença, o elif vai garantir que aquela condição seja verificada caso o If seja falso, diferente dos dois If que são 'fluxos' independentes.





if = se
elif = se não
else = não
