# O QUE É LISTA

# COMO CRIAR UMA LISTA


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


