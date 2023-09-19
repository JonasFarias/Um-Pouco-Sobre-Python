# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input('Qual o ano de seu Nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano
saldo = 18 - idade

print('-=-' * 10)
print('ALISTAMENTO MILITAR')
print('-=-' * 10)

# verifica se o usuario é menor de idade indica em que ano ele tem que se alistar
if idade <= 17:
    print('''Quem nasceu em {}, tem {} não precisa se alistar
    o seu ano de alistamento é {}'''.format(ano, idade, (saldo + ano_atual)))

    # se o usuario for maior de 18, ele mostra em que ano ele deveria ter se alistado
elif idade >= 18:


    print('\n\nVocê já deveria ter se ALISTADO em {}'.format((ano + 18 )))