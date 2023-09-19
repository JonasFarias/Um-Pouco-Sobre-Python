'''Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120'''

from time import sleep
numero = int(input('Digite um numero: '))
contador = numero
fatorial = 1
print('Calculando  Fatorial de {}!'.format(numero))
sleep(5)
while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print('{}'.format(fatorial))

