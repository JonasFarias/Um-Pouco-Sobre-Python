'''

Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO,
OPCIONAL e OBRIGATÓRIO nas eleições.
'''




def voto(ano):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano

    if idade >= 65:
        print(f'Você tem {idade} anos, seu voto é OPCIONAL!')

    elif idade >= 18:
        print(f'Você tem {idade} anos, seu voto é OBRIGATÓRIO!')

    elif idade >= 16:
        print(f'Você tem {idade} anos, seu voto é OPCIONAL!')

    elif idade < 16:
        print(f'Você tem {idade} anos, não tem idade sufiiente para Votar!!')

    return idade


ano_nascimento = int(input('Qual seu ano de nascimento: '))
voto(ano_nascimento)
