# INSTALAÇÃO DA BIBLIOTECA KIVY NO AMBIENTE WINDOWS

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
