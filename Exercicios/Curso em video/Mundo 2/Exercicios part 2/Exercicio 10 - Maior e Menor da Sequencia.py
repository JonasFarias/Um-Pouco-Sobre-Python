# Faça um programa que leia o peso de cinco
# pessoas. No final, mostre qual foi o maior e o menor peso lidos.

# contadores maior e mnor
maior = 0
menor = 0

#repetição do input
for pessoa in range(1, 6):
    peso = float(input('Qual o peso da {}ª pessoa:'.format(pessoa)))

# se o contador for == 1 adiciona os valores as variaveis
    if pessoa == 1:
        maior = peso
        menor = peso
# se não verifica se os contadores são maiores e menores e substitui o valor
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
# exibe na tela
print(' O maior peso lido é {}Kg'.format(maior))
print(' O menor peso lido é {}Kg'.format(menor))