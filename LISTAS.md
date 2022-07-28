# O QUE É LISTA

Uma lista é uma coleção de itens.
Você pode colocar qualquer informação que quiser em uma lista, e os itens de sua lista não precisam
estar relacionados de nenhum modo em particular. 
Como uma lista geralmente contém mais de um elemento, é uma boa ideia deixar seu nome
no plural, por exemplo, letras, digitos ou nomes.
Eis um exemplo simples de uma lista que
contém alguns tipos de doces:

``` 
# criamos a lista de doces
doces = ['Chocolate', 'Sorvete', 'Pudim']
# mandamos mostrar nossa lista atual
print(doces)
```

# COMO CRIAR UMA LISTA

Em Python, colchetes ([]) indicam uma lista, e elementos individuais da
lista são separados por vírgulas.
Exemplo: <br/>
`doces = []`

Podemos também criar uma lista da seguinte maneira.<br/>
`doces = list()`
as duas formas a cima criamos uma lsita totalmente vazia. podemos já criar uma lista com dados dentro dela, da seguinte forma!<br/>
`
doces = ['Chocolate', 'Sorvete', 'Pudim']
`<br/>
ou<br/>
`
doces = list(['Chocolate', 'Sorvete', 'Pudim'])
`


# Alterando, acrescentando e removendo elementos

A maioria das listas que você criar será dinâmica, o que significa que sua lista pode ter 
elementos adicionados ou removidos de acordo com a necessidade do seu programa.

## MODIFICANDO LISTAS
A sintaxe para modificar um elemento é semelhante à sintaxe para acessar
um elemento de uma lista. Para alterar um elemento, use o nome da lista
seguido do índice do elemento que você quer modificar e, então, forneça o
novo valor que você quer que esse item tenha.

Exemplo, vamos criar uma lista de doces, e que o
primeiro item da lista seja 'chocolate'. 
Como mudaríamos o valor desse primeiro item?

``` 
# criamos a lista de doces
doces = ['Chocolate', 'Sorvete', 'Pudim']
# mandamos mostrar nossa lista atual
print(doces)
# motificamos o primeiro item da lista pelo item brigadeiro
doces[0] = 'brigadeiro'
# mandamos mostrar a lista atualizada de doces com o novo valor
print(doces) 
```

O codigo acima terá a saida:
```
# nossa primeira lita
['Chocolate', 'Sorvete', 'Pudim']
# nossa lista atualizada
['brigadeiro', 'Sorvete', 'Pudim']
```
Você pode mudar o valor de qualquer item de uma lista, e não apenas o
primeiro.

# Acrescentando elementos em uma lista

Você pode adicionar  um item na lista utilizando o comando .append
Exemplo:

```
# Nossa lista atual de doces
doces = ['Chocolate', 'Sorvete', 'Pudim']
print(doces)
# Aqui estamos adicionando mais um elementeo a nossa lista
doces.append('brigadeiro')
print(doces)
```

Diferente do codigo anterior, em vez de modificarmos um item da lista estamos acrescentando um item a lista
então nosso novo codigo em vez de substituir o 'Chocolate' por 'Brigadeiro' ele vai acrescentar o 'Brigfadeiro' ao final da nossa lsita.

O método append() acrescenta 'Brigadeiro' no final da lista sem afetar
qualquer outro elemento:
```
['Chocolate', 'Sorvete', 'Pudim']
['Chocolate', 'Sorvete', 'Pudim', 'Brigadeiro']

```
O método append() facilita criar listas dinamicamente. Por exemplo,
podemos começar com uma lista vazia e então acrescentar itens à lista
usando uma série de instruções append().

## Removendo elementos de uma lista
Você vai querer remover um item ou um conjunto de itens
de uma lista.
Se um usuário decidir cancelar a conta em sua aplicação
web, você vai querer remover esse usuário da lista de usuários ativos. 
Removendo um item usando a instrução `del`
Se a posição do item que você quer remover de uma lista for conhecida, a
instrução del poderá ser usada.

```
doces = ['Chocolate', 'Sorvete', 'Pudim']
print(doces)
del doces[0]
print(doces)

```

Usamos del para remover o primeiro item, 'Chocolate', da lista de
doces:

```
['Chocolate', 'Sorvete', 'Pudim']
['Sorvete', 'Pudim']

```

Você pode remover um item de qualquer posição em uma lista usando a
instrução del, se souber qual é o seu índice. Por exemplo, eis o modo de
remover o segundo item, 'Sorvete', da lista:
doces = ['Chocolate', 'Sorvete', 'Pudim']
print(doces)
del doces[1]
print(doces)
O segundo Doce é apagada da lista:
['Chocolate', Sorvete', 'Pudim']
['Chocolate', 'Pudim']

Nos dois exemplos não podemos mais acessar o valor que foi removido
da lista após a instrução del ter sido usada.

#### Removendo um item com o método pop()

Em algum momento você vai querer usar o valor de um item depois de removê-lo
de uma lista. Em uma aplicação web, você poderia remover
um usuário de uma lista de membros ativos e então adicioná-lo a uma
lista de membros inativos.
O método `pop()` remove o último item de uma lista, mas permite que
você trabalhe com esse item depois da remoção. 
Vamos fazer um pop de um doce da lista de docess: 
```

# Criamos nossa lista de doces
doces = ['Chocolate', 'Sorvete', 'Pudim']
# Exibimos nossa lista de doces
print(doces)
# criamos uma variavel, para receber os doces "apagados"
doces_removidos = doces.pop()
# Mostramos a lista de doces
print(doces) 
# Aqui exibimos os doces "apagados"
print(doces_removidos) 
```

A saída mostra que o valor 'Pudim' foi removido do final da lista e
agora está armazenado na variável doces_removidos: 
```
['Chocolate', 'Sorvete','Pudim']
['Chocolate', 'Sorvete']
Pudim
```

Lembre-se de que, sempre que usar `pop()`, o item com o qual você
trabalhar não estará mais armazenado na lista.
Se você não tiver certeza se deve usar a instrução `del` ou o método
`pop()`, eis um modo fácil de decidir: quando quiser apagar um item de
uma lista e esse item não vai ser usado de modo algum, utilize a
instrução `del`; se quiser usar um item à medida que removê-lo, utilize o
método `pop()`.

### Removendo um item deacordo com o valor
Às vezes, você não saberá o indice do item que quer apagar, apenas o valor do item que deseja remover, o método
`remove()` poderá ser usado.
Por exemplo, vamos supor que queremos remover o valor 'Brigadeiro' da
lista de doces.
```doces = ['Chocolate', 'Sorvete', 'Pudim', 'Brigadeiro']
print(doces)
doces.remove('Brigadeiro')
print(doces)
```
O código em diz para o Python para descobrir em que lugar 'Brigadeiro' aparece na lista e remover esse
elemento: 
```
['Chocolate', 'Sorvete', 'Pudim', 'Brigadeiro']
['Chocolate', 'Sorvete', 'Pudim']
```
Também podemos usar o método `remove()` para trabalhar com um
valor que está sendo removido de uma lista. 

### NOTA 
O método `remove()` apaga apenas a primeira ocorrência do valor que
você especificar. 

### Percorrendo uma lista inteira com um laço
Com frequência, você vai querer percorrer todas as entradas de uma
lista, executando a mesma tarefa em cada item. Por exemplo, em uma lista de números, talvez você queira executar a
mesma operação estatística em todos os elementos. 
Quando quiser executar a mesma ação em todos os itens de uma lista,
você pode usar o laço `for` de Python .<br />
Vamos supor que temos uma lista de nomes de times e queremos
exibir todos os nomes da lista. <br />

Vamos usar um laço `for` para exibir cada um dos nomes de uma lista
de times: <br />


```
# Começamos definindo uma lista de times
times = ['corinthians', 'palmeiras', 'santos']
# Definimos um laço para extrair o nome da lista times e amarzenar na variavel time
for time in times: 
# pedimos para exibir o nome que foi armazenado na variavel time
  print(time) 

```
 O interpretador então repete as linhas uma vez para cada nome da lista. 
Ler esse código como <br />
“para todo time na lista de times, exiba o nome do time” pode ajudar. 
A saída é uma exibição simples de cada nome da lista: 
```
corinthians
palmeiras
santos
```

### Observando os laços com mais detalhes

O conceito de laços é importante porque é uma das maneiras mais
comuns para um computador automatizar tarefas repetitivas. 
Por
exemplo, em um laço simples como o que usamos em times.py,
Python inicialmente lê a primeira linha do laço: 
`for time in times:` Essa linha diz ao Python para extrair o primeiro valor da lista
times e armazená-lo na variável time. O primeiro valor é `'corinthians'`.
O interpretador então lê a próxima linha: `print(time)` O Python exibe o
valor atual de time, que ainda é 'corinthians'. 
Como a lista contém mais valores, o interpretador retorna à primeira linha do laço: 
`for time in times : ` Python recupera o próximo nome da lista, que é 'palmeiras', e
armazena esse valor em time. Então ele executa a linha:
`print(time)` Python exibe o valor atual de time, que agora é
'palmeiras', novamente. O interpretador repete todo o laço mais uma vez
com o último valor da lista, que é 'santos'. Como não há mais valores
na lista, Python passa para a próxima linha do programa. Nesse caso,
não há mais nada depois do laço `for`, portanto o programa simplesmente
termina.
Quando usar laços pela primeira vez, tenha em mente que o conjunto
de passos será repetido, uma vez para cada item da lista, não importa
quantos itens haja na lista. Se você tiver um milhão de itens em sua lista,
Python repetirá esses passos um milhão de vezes – e geralmente o fará
bem rápido.
Tenha em mente também que quando escrever seus próprios laços `for`,
você poderá escolher qualquer nome que quiser para a variável
temporária que armazena cada valor da lista. No entanto, é conveniente
escolher um nome significativo, que represente um único item da lista.

Por exemplo, eis uma boa maneira de iniciar um laço `for` para uma lista
de gatos, uma lista de cachorros e uma lista genérica de itens: 
`for gato in gatos:` <br />
`for cachorro in cachorros:` <br />
`for item in lista_de_itens:`<br />
Essas convenções de nomenclatura podem ajudar você a acompanhar a ação executada em
cada item em um laço `for`. O uso de nomes no singular e no plural pode
ajudar a identificar se a seção de código atua em um único elemento da
lista ou em toda a lista.

### Criando listas numéricas
Em visualizações de dados, quase sempre você trabalhará com conjuntos de números, como
temperaturas, distâncias, tamanhos de população ou valores de latitudes
e longitudes, entre outros tipos de conjuntos numéricos.
As listas são ideais para armazenar conjuntos de números, e Python
oferece várias ferramentas para ajudar você a trabalhar com listas de
números de forma eficiente. Depois que souber usar efetivamente essas
ferramentas, seu código funcionará bem, mesmo quando suas listas
tiverem milhões de itens.

#### Estatísticassimplescomumalista de números
Algumas funções Python são específicas para listas de números. Por
exemplo, podemos encontrar facilmente o valor mínimo, o valor
máximo e a soma de uma lista de números: 

```
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(numeros))
print(max(numeros))
print(sum(numeros))
```
```
0
9
45
```

NOTA Os exemplos desta seção utilizam listas pequenas de números para
que caibam facilmente na página. Esses exemplos também funcionarão
bem se sua lista contiver um milhão de números ou mais.


### Fatiando uma lista
Para pegarmos parte de uma lista devemos, especificar o índice do primeiro e do último
elemento com os quais queremos trabalhar. 
Como ocorre na função `range()`, Python para em um item antes do segundo índice que você
especifica. Para exibir os três primeiros elementos de uma lista, solicite
os índices de 0 a 3; os elementos 0, 1 e 2 serão devolvidos.
O exemplo a seguir envolve uma lista de cervejas de um bar:

```
cervejas = ['skol', 'bhrama', 'imperio', 'heineken', 'itaipava']

print(cervejas[0:3]) 
```
O código exibe uma fatia dessa lista, que
inclui apenas as três primeiras cervejas. A saída mantém a estrutura de
lista e inclui as três primeiras cervejas: ```['skol', 'bhrama', 'imperio',]```


Uma fatia que inclua o final de uma lista. Por exemplo, se quiser todos os itens do terceiro até
o último item, podemos começar com o índice 2 e omitir o segundo
índice: 
```
cervejas = ['skol', 'bhrama', 'imperio', 'heineken', 'itaipava']
print(cervejas[2:]) 
```
Python devolve todos os itens, do terceiro item até o
final da lista: `['imperio', 'heineken', 'itaipava']`
Essa sintaxe permite apresentar todos os elementos a partir de
qualquer ponto de sua lista até o final, independentemente do tamanho
da lista. 
um índice negativo devolve um elemento a
uma determinada distância do final de uma lista; assim, podemos exibir
qualquer fatia a partir do final de uma lista. 
```
cervejas = ['skol', 'bhrama', 'imperio', 'heineken', 'itaipava']
print(cervejas[-3:]) 
```
Esse código exibe os nomes dos três últimos jogadores
e continuaria a funcionar à medida que a lista de jogadores mudar de
tamanho.

fontes

* curso em video
* curso intesivo de python uma introdução...
