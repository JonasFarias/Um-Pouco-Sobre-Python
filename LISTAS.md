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





fontes

* curso em video
* curso intesivo de python uma introdução...
