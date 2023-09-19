'''
Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais: o nome de um jogador e
quantos gols ele marcou. O programa deverá ser capaz de mostrar
a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''

def ficha(nome=None, gol=None):
    if nome == None and gol == None:
        return 'Sem jogador cadastrado'
    else:
        return f'O Jogador {nome}, fez {gol} Gols no campeonato!'

jogador = input('Registrar Jogaddor: ')
gol = input('Gols no campeonato: ')

if jogador == '':
    print(ficha())
else:
    print(ficha(jogador, gol))