'''
Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
from time import sleep

def maior(* num):
    contador = maior = 0
    print('=-' * 30)
    print('Analisando os Valores passados... ')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1
    print(f'\nForam passados {contador} valores')
    print(f'E o maior valor foi {maior}')




maior(9,8,7,6,5,4,1,2,)
maior(6,3,8,7,2,1,)
maior(3,5,6,7,)
maior(3)
maior(2)