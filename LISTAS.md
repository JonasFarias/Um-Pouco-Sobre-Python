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
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
u del motorcycles[0]
print(motorcycles)
O código em u usa del para remover o primeiro item, 'honda', da lista de
motocicletas:
['honda', 'yamaha', 'suzuki']
['yamaha', 'suzuki']








fontes

curso em video
curso intesivo de python uma introdução...
