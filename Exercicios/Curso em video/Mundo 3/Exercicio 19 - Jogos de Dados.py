'''Crie um programa onde 4 jogadores joguem um dado e
tenham resultados aleatórios. Guarde esses resultados
em um dicionário em Python. No final, coloque esse dicionário
em ordem, sabendo que o vencedor tirou o maior número no dado.'''


from random import randint
from time import sleep
from operator import itemgetter
jogos = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}
ranking = {}
for chave, valor in jogos.items():
    sleep(1)
    print(f'{chave}, jogou o dado: {valor}')
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)

print('=-' * 20)
for indice, valor in enumerate(ranking):
    sleep(1)
    print(f'{indice+1}º Lugar {valor[0]} com: {valor[1]}')


