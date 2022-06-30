TUPLAS

Variáveis compostas(TUPLAS)

Tuplas tem uma diferença das listas em Python,  são imutáveis. 
Tuplas são ideais para representar listas de valores constantes e também para realizar opções de empacotamento e desempacotamento de valores.
Primeiramente, vejamos como criar uma tupla.

tupla = (“a”, “b”, “c”)
tupla
(‘a’, ‘b’, ‘c’)

Tuplas suportam a maior parte das operações de lista, como fatiamento e indexação.
mas tuplas não pode ter seus elementos alterados.

tupla[0]
‘a’
tupla[2]
‘c’
tupla[1:]
(‘a’, ‘c’)
len(tupla)
3


Varias funções utilizam ou geram tuplas em Python.
elas podem ser utilizadas com o for

lanche = ‘Hamburguer’, ‘suco’, ‘pudim’, ‘pizza’

‘’’MANEIRA MAIS SIMPLES DE MOSTRAR OS ITENS DA TUPLA’’’

for comida in lanche:
	print(‘fEu vou comer {comida} ‘)


‘’’ MANEIRA USANDO O RANGE, PARA ENUMERAR OS ITENS DA TUPLA’’’

for contador in range(0, len(lanche)):
	print(‘fEu vou comer {lanche[cont]} na posição {contador}’)


‘’’MANEIRA USANDO O ENUMARATE’’’

for posicao, comida in enumerate(lanche):
	print(f’Eu vou comer {comida} na posição {posição}’)

print(‘Comi pra caramba!’)


Python permite criarmos tuplas separados por virgula, independente de usarmos parênteses:

tupla =100, 200, 300
tupla
(100, 200, 300)

100, 200, 300 foram convertidos em tupla com três elementos.
Esse tipo de operação é chamado de empacotamento.
Tuplas podem ser utilizadas para desempacotar valores.

Exemplo

a, b = 10, 20
a
10
b
20


Tuplas também podem ser criadas a partir de uma lista com a função tuple:
Ex:
l = [1, 2, 3]
t = tuple(l)
t
(1, 2, 3)

Não podemos alterar tuplas após a sua criação, mas podemos concatená-las
criando novas tuplas:

tupla1 = 1, 2, 3
tupla2 = 1, 2, 3
tupla1 + tupla2
tupla3 = 1, 2, 3, 1, 2, 3


Se uma tupla contiver uma lista ou outro objeto que pode ser alterado,
este continuará a funcionar normalmente. Veja o exemplo de uma tupla
que contém uma lista:

tupla = (‘a’, [‘b’, ‘c’, ‘d’])
tupla 
(‘a’, [‘b’, ‘c’, ‘d’])


Nada mudou na tupla em si, mas na lista que é seu segundo elemento.
A tupla não foi alterada, mas a lista que ela continha, sim.
len(tupla)
2
tupla[1]
[‘b’, ‘c’, ‘d’]
tupla[1].append(‘e’)
tupla
(‘a’, [‘b’, ‘c’, ‘d’, ‘e’])


