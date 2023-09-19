# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))
numero3 = int(input('Digite o ultimo numero: '))

# verificando o menor numero
menor = numero1

if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero1 and numero3 < numero2:
    menor = numero3

#verificando o maior numero
maior = numero1

if numero2 > numero1 and numero2 > numero3:
    maior = numero2
if numero3 > numero1 and numero3 > numero2:
    maior = numero3

print('O menor numero é: {}'.format(menor))
print('O Maior numero é: {}'.format(maior))