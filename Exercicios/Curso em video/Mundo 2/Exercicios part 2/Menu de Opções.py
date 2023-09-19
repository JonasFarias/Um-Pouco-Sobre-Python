'''Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep

numero1 = int(input('Valor 1: '))
numero2 = int(input('Valor 2: '))
opcao = 0

while opcao != 7:
    print('#' * 30)
    print('''        [ 1 ] SOMAR
        [ 2 ] MULTIPLICAR
        [ 3 ] SUBTRAIR
        [ 4 ] DIVIDIR
        [ 5 ] MAIOR
        [ 6 ] NOVOS NÚMEOS
        [ 7 ] SAIR DO PROGRAMA''')

    print('#' * 30)
    opcao = int(input('Qual a sua opção: '))
    if opcao == 1:
        print('{} + {} = {}'.format(numero1, numero2, numero1 + numero2))
    elif opcao == 2:
        print('{} x {} = {}'.format(numero1, numero2, numero1 * numero2))
    elif opcao == 3:
        print('{} - {} = {}'.format(numero1, numero2, numero1 - numero2))
    elif opcao == 4:
        print('{} / {} = {}'.format(numero1, numero2, numero1 / numero2))
    elif opcao == 5:
        if numero1 > numero2:
            print('O Maior numero é: {}'.format(numero1))
        else:
            print('O Maior numero é: {}'.format(numero2))
    elif opcao == 6:
        print('Digite novos valores!')
        numero1 = (int(input('Valor 1: ')))
        numero2 = (int(input('Valor 2: ')))
    elif opcao == 7:
        print('Finalizando o programa...')
        sleep(3)

    else:
        print('Opção Invalida')


