# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.


numero = int(input('Digite um numero: '))
tot = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        tot += 1
        print('\033[34m', end=' ')
    else:
        print('\033[33m', end=' ')
    print('{}'.format(c), end=' ')

print('\n\033[0mO {} foi divisivel {} vezes, por isso não é PRIMO!'.format(numero,tot))
