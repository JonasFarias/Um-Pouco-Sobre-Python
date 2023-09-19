'''
Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo. Seu programa tem que realizar
três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''

from time import sleep

def linha():
    print('-=' * 20)

def contator(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    linha()
    print(f'contando do {inicio}, até {fim} em {passo} a {passo}')
    sleep(2.5)
    cont = inicio

    if inicio < fim:
        while cont <= fim:
            print(f'{cont}', end=' ')
            cont += passo
            sleep(0.3)
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ')
            cont -= passo
            sleep(0.3)
    print('FIM')
contator(1, 10, 1)
contator(10, 0, 2)

print('Fazer uma contagem Personalizada')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contator(inicio, fim, passo)

