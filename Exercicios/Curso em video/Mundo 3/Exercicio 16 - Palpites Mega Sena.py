'''Faça um programa que ajude um jogador da MEGA SENA
a criar palpites.O programa vai perguntar quantos jogos
serão gerados e vai sortear 6 números entre 1 e 60 para cada
jogo, cadastrando tudo em uma lista composta.'''


print('=' * 20)
print('     MEGA SENA   ')
print('=' * 20)

from random import randint
from time import sleep

lista = []
total_sorteios = []
quantidade = int(input('Quantas simulações você quer fazer: '))
total = 1
while total <= quantidade:
    contador = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    total_sorteios.append(lista[:])
    lista.clear()
    total += 1

print(f'=' * 10, f'SORTEANDO {quantidade}', '=' * 10)

for indice, lista in enumerate(total_sorteios):
    print(f'Jogo {indice+1}º, {lista}')
    sleep(1)
print('-=' * 5,'BOA SORTE', '-=' * 5)

