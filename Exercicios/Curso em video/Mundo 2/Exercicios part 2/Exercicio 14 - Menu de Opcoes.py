''' Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep

finalizar = False
valor_1 = int(input('Primeiro valor: '))
valor_2 = int(input('Segundo valor: '))
while not finalizar:
    print('[ 1 ] SOMAR')
    print('[ 2 ] MULTIPLICAR')
    print('[ 3 ] MAIOR')
    print('[ 4 ] NOVOS NÚMEROS')
    print('[ 5 ] SAIR DO PROGRAMA')
    escolha = int(input('>>>>>> Qual sua escolha: '))
    if escolha == 4:
        valor_1 = int(input('Digite um novo valor: '))
        valor_2 = int(input('Digite um novo valor: '))

    elif escolha == 2:
        multiplicar = valor_1 * valor_2
        print('O {} Multiplicado por {} é igual a: {}'.format(valor_1, valor_2, multiplicar))
    elif escolha == 3:
        if valor_1 > valor_2:
            print('Entre {} e {} o maior é:{}'.format(valor_1, valor_2, valor_1))
        else:
            print('Entre {} e {} o maior é: {}'.format(valor_1, valor_2, valor_2))
    elif escolha == 1:
        soma = valor_1 + valor_2
        print('A soma do {} e {} é de: {} '.format(valor_1, valor_2, soma))
    elif escolha == 5:
        print('Finalizando progragama...')
        sleep(2)
        finalizar = True
    else:
        if escolha != 1 and 2 and 3 and 4 and 5:
            print('Opção invalida digite novamente: ')

print('Obrigado até a proxima!!')
