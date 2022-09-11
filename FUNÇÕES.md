vamos continuar nossos estudos de 
funções em Python, aprendendo mais 
sobre Interactive Help em Python, o 
uso de docstrings para documentar nossas 
funções, argumentos opcionais para dar mais 
dinamismo em funções Python, 
escopo de variáveis e retorno de resultados.



## PARAMETROS OPCIONAIS

Vamos pensar em uma funcionalidade de que some 3 numeros
`somar(1,2,3)`
Como criariamos uma função para essa funcionalidade

```
def somar(a,b,c):
    s = a + b + c
    print(f'A somda dos valores é {s}')   
```
onde
a seria 1
b seria 2
c seria 3
respectivamente em sua ordem da esquerda para direita

mas o o que será que acontece se colocassemos menos parametros
exe:
agora temos 
`somar(1, 2, 3)`
e se fosse
`somar(1, 2)`
o que acontecesseria?
o 1 ficaria em a <br> 
o 2 ficaria em b <br>
porém quem ficaria no lugar do c
```
a seria 1
b seria 2
c seria ?
```
acontece que o c não teria valor o que ocasionária um problema
na chamada da função
a não ser que usassemos o conceito de parâmetros opcionais

o que podemos fazer 
```commandline
def somar (a,b,c=0):
    s = a + b + c
    print(f'A soma dos numeros é de {s}')
```
O que significa isso que se por acaso o valor c não for preenchido
ele vai valer 0
onde
a seria 1 <br>
b seria 2 <br>
c seria 0 <br>

e agora nossa função vai funcionar normalmente
como funcionaria também se fissemos assim
```commandline
def somar (a=0,b=0,c=0):
    s = a + b + c
    print(f'A soma dos numeros é de {s}')
```
idependente de qual posição for colocada podemos definir o seu valor
assim caso não seja informado, nosso programa funcionara
como podemos também chamar a função assim
`somar(c=1, b=2, a=1)`
que vai funcionar também com cada um recebendo seus valores 


## RETORNO DE RESULTADOS

return

funções que retornam valores são mais uteis para personalização de resultados