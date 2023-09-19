'''Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''

while True:
    print('-' * 30)
    tabuada = int(input('Quer ver qual Tabuada: '))
    print('-' * 30)
    if tabuada < 0:
        print('PROGRAMA TABUADA ENCERRADO!!')
        break
    for contador in range (1, 11):
        print(f'{tabuada} X {contador} = {tabuada * contador}')

