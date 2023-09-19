'''Crie um programa onde o usuário possa digitar
sete valores numéricos e cadastre-os em uma lista
única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.'''


numeros = [[], []]
contador = 0
valor = 0
for contadora in range(1, 8):
    contador += 1
    valor = (int(input(f'Digite o {contador}º numero: ')))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores Pares digitados foram {numeros[0]}.')
print(f'Os valores Impares digitados foram {numeros[1]}')
