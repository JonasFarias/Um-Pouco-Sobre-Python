'''Crie um programa que vai ler vários números
e colocar em uma lista. Depois disso,
crie duas listas extras que vão conter apenas os
valores pares e os valores
ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

lista = []
par = []
impare = []
while True:
    lista.append(int(input('Digite um numero: ')))
    resposta = str(input('Quer continuar [S/N]')).strip().upper()[0]
    if resposta in 'N':
        break
for index, valor in enumerate(lista):
    if valor % 2 == 0:
        par.append(valor)
    else:
        impare.append(valor)
print(f'A lista completa é {lista}')
print(f'Na lista os numeros pares são {par}')
print(f'Na lista os numeros impares são {impare}')
