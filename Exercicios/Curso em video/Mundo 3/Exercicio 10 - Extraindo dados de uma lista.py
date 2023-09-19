'''Crie um programa que vai ler vários números e
colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

numeros = []
contador = 0
while True:
    numero = int(input('Digite um valor: '))
    numeros.append(numero)
    resposta = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if resposta in 'N':
        break
print(f'Foram digitados {len(numeros)} numeros e os valores digitados foram {numeros}')
numeros.sort(reverse=True)
print(f'Os Numeros em ordem Decrescente são: {numeros}')
numeros.sort()
print(f'Os numeros em ordem Crescente são: {numeros}')
if 5 in numeros:
    print('O valor 5 costa na lista')
else:
    print('O Valor 5 não consta na lista')
