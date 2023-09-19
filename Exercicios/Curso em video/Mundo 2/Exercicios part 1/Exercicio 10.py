# Crie um programa que faça o computador jogar Jokenpô com você.

#importa da biblioteca random a opção choice, para podermos fazer a escolha randomica

import random


# escolhe dentro da bibliotea time a opção sleep, para podermos desacelerar o programa na hora do jo ken po!!
from time import sleep


#INDICE
print('#' * 20)
print('\n      JO KEN PO\n')
print('#' * 20)

# MOSTRA AS OPÇÕES DISPONIVEIS PARA JOGAR
print('''
Suas opções:
[ 1 ] PEDRA 
[ 2 ] PAPEL
[ 3 ] TESOURA
''')

# DEFINE AS OPÇÕES
escolha = [1, 2, 3]

# FAZ O COMPUTADOR ESCOLHER ENTRE UMA DAS OPÇÕES
computador = random.choice(escolha)

# PEDE PARA O JOGADOR ESCOLHER ENTRE AS OPÇÕES
jogador = int(input('Qual a sua escolha: '))

# VERIFICA SE O JOGADOR ESCOLHE UMA DAS OPÇÕES DISPONIVEIS
if jogador != 1 and jogador != 2 and jogador != 3:
    # SE NÃO FOR DISPONIVEL ELE AVISA QUE A OPÇÃO NÃO É VALIDA
    print('OPÇÃO INVALIDA')
    # SE FOR UMA OPÇÃO VALIDA, ELE DA CONTINUIDADE NO JOGO
else:
    print('\nJO\n')
    sleep(1)
    print('KEN\n')
    sleep(1)
    print('PO!!\n')


# COMPARA AS JOGADAS PARA DEFINIR O VENCEDOR E PERDEDO OU SE AH EMPATE
if jogador == 1 and computador == 2:

    print('-=-' * 15)
    print('O computador GANHOU, ele escolheu PAPEL:')
    print('-=-' * 15)

elif jogador == 2 and computador == 3:

    print('-=-' * 15)
    print('O Computador GANHOU, ele escolher TESOURA:')
    print('-=-' * 15)

elif jogador == 3 and computador == 1:

    print('-=-' * 15)
    print('O Computador GANHU, ele escolheu PEDRA:')
    print('-=-' * 15)

elif jogador == 1 and computador ==3:

    print('-=-' * 15)
    print('PARABÉNS, você escolheu PEDRA e\n o computador escolheu TESOURA')
    print('-=-' * 15)

elif jogador == 2 and computador == 1:

    print('-=-' * 15)
    print('PARABÉNS, você escolheu PAPEL e\n o computador escolheu PEDRA')
    print('-=-' * 15)

elif jogador == 3 and computador == 2:

    print('-=-' * 15)
    print('PARABÉNS, você escolheu TESOURA e\n o computador escolheu PAPEL')
    print('-=-' * 15)

elif jogador == 1 and computador == 1:

    print('-=-' * 5)
    print('     EMPATE')
    print('-=-' * 5)

elif jogador == 2 and computador == 2:

    print('-=-' * 5)
    print('     EMPATE')
    print('-=-' * 5)

elif jogador == 3 and computador == 3:

    print('-=-' * 5)
    print('     EMPATE')
    print('-=-' * 5)
