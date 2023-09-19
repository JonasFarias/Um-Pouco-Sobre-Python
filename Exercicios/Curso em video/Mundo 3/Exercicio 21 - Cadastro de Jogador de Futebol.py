'''
 Crie um programa que gerencie o aproveitamento de um jogador de futebol.
 O programa vai ler o nome do jogador e quantas partidas ele jogou.
 Depois vai ler a quantidade de gols feitos em cada partida.
 No final, tudo isso será guardado em um dicionário, incluindo o total de
 gols feitos durante o campeonato.
'''

jogador = {}
gols = []
total_gols = []
jogador['nome'] = str(input('Nome do Jogador: '))
jogador['jogos'] = int(input('Quantos jogos ele participou: '))
numero_de_jogos = jogador['jogos']
contador = 0
jogos = 0
while contador < numero_de_jogos:
    contador += 1
    jogos += 1
    numero_de_gols = int(input(f'numero de gol no jogoº {jogos}: '))
    gols.append(numero_de_gols)
    total_gols.append(gols[:])
    gols.clear()

print('=- ' * 30)

jogador['gols'] = total_gols
print(jogador)
print('=- ' * 30)
print(f'O jogador {jogador["nome"]}, jogou {numero_de_jogos} jogos')
print('=- ' * 30)
for indice, gol in enumerate(total_gols):
    print(f'Na paritda {indice + 1}, {jogador["nome"]} fez {gol} gol´s')
print('=- ' * 30)
