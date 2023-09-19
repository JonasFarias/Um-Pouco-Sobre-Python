# Crie um programa que leia o ano de nascimento
# de sete pessoas. No final, mostre quantas
# pessoas ainda não atingiram a maioridade e quantas já são maiores.

# BIBLIOTECA PARA PUXAR A DATA ATUAL
from datetime import date
# ARMAZENA ANO ATUAL
ano_atual = date.today().year

maior = 0
menor = 0
contador = 0

for c in range(1, 9):
    contador = contador + 1
    pessoa = int(input(' qual idade da {}ª pessoa: '.format(contador)))
    pessoa = int(pessoa + 1)
    if (ano_atual - pessoa) >= 21:
        maior += 1
    else:
        menor += 1
print('Tem {} pessoas maiores de idade: '.format(maior))
print('Tem {} pessoas menores de idade: '.format(menor))