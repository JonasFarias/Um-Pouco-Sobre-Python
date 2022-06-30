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

