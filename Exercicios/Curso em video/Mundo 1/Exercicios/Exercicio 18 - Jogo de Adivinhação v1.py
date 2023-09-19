#  Escreva um programa que faça o computador
#  "pensar" em um número inteiro entre 0 e 5 e peça para o
#  usuário tentar descobrir qual foi o número escolhido pelo computador. O
#  programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
import random

numero = int(input('Tente adivinhar em que numero eu pensei entre 0 e 5:'))
n1 = 0
n2 = 1
n3 = 2
n4 = 3
n5 = 4
n6 = 5

numeros_para_adivinhar = [n1, n2, n3, n4, n5, n6]
tente_me_adivinhar = random.choice(numeros_para_adivinhar)

print('PROCESSANDO')

if numero == tente_me_adivinhar:
    print('Parabéns você ganhou o jogo, adivinhando o numero que eu pensei:')

else:
    print('você não acertou o numero: desculpe tente outra vez! eu pensei no numero {}: '.format(tente_me_adivinhar))


"""
from random import randint  #importa a função randint da biblioteca random

computador = randint(0, 5)

print('-=-' * 15)
print(('VOU PENSAR EM UM NUMERO TENTE ADIVINHAR'))
print('-=-' * 15)
jogador = int(input('Tente adivinhar o numero que eu pensei: '))

if jogador == computador:
    print('Parabéns, você ganhou!!')
else:
    print('Desculpa você perdeu, eu pensei no numero {} e não {}'.format(computador, jogador))
