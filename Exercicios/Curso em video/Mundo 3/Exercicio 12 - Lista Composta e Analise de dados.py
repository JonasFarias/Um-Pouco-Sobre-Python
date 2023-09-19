'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

#lista temporaria criada para receber os dados
temporario = []
#lista principal, que sera usada para mostrar os dados
principal = []
#variavel para armazenar o maior peso
maior = 0
#variavel para armazenar o menor peso
menor = 0

#Lopping infinito para receber os dados
while True:
    #adiciona o nome da pessoa na lista temporaria
    temporario.append(str(input('Nome: ')))
    #adiciona o peso na lista temporaria
    temporario.append(float(input('Peso: ')))
    #verifica se é o primeiro valor a ser adicionado na lista
    if len(principal) == 0:
        #atipui o valor da lista temporaria nas variaveis maior e menor
        maior = temporario[1]
        menor = temporario[1]
        #verifica se os valores da lista são maiores ou menores para fazer a nova atribuição
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]
            #faz uma copia da lista temporaria para a principal
    principal.append(temporario[:])
    #limpa a lista temporaria
    temporario.clear()
    resposta = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resposta in 'N':
        break

print('=' * 30)
print(f'Ao todo foram cadastrado {len(principal)} pessoas.')
print(f'O maior peso cadastrado é {maior}Kg. Peso de ', end='')
for pessoas in principal:
    if pessoas[1] == maior:
        print(f'[{pessoas[0]}] ', end='')
print()
print(f'O menor peso cadastrado é {menor}Kg. Peso de ', end='')
for pessoas in principal:
    if pessoas[1] == menor:
        print(f'[{pessoas[0]}] ', end='')
print()