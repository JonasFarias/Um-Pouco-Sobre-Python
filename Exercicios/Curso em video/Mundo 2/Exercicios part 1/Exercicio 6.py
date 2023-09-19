# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import date

ano_atual = date.today().year

print('-=-' * 10)

print('  CLASSIFICAÇÃO DE NADADORES')

print('-=-' * 10)

nascimento = int(input('Qual seu ano de nascimento:'))

if (ano_atual - nascimento) <= 9:
    print('\n\n\nNADADOR MIRIM\n\n\n')
elif (ano_atual - nascimento) <= 14:
    print('\n\n\nNADADOR INFANTIL\n\n\n')
elif (ano_atual - nascimento) <= 19:
    print('\n\n\nNADADOR JUNIOR\n\n\n')
elif ano_atual - nascimento <= 25:
    print('\n\n\nNADADOR SENIOR\n\n\n')
else:
    print('\n\n\nNADADOR MASTER\n\n\n')


print('-=-' * 10)
print('-=-' * 10)