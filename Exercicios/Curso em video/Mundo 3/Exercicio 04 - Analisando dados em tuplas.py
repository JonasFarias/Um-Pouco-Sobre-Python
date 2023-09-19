'''Desenvolva um programa
que leia quatro valores
pelo teclado e guarde-os
em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''


numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))
numero3 = int(input('Digite mais um numero: '))
numero4 = int(input('Digite o ultimo numero: '))

numeros = numero1, numero2, numero3, numero4

print(f'O numero 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'o numero 3 apareceu na {numeros.index(3)+1}ª posição.')
else:
    print('O numero 3 não foi digitado!')
print(f'Os numeros pares digitados são', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')


