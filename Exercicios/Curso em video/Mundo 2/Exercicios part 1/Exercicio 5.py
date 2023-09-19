# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

matematica = float(input('Digite sua nota de Matematica: !'))
portugues = float(input('Digite sua nota de Português: '))
ciencias = float(input('Digite sua nota de Ciencias: '))

media = (matematica + portugues + ciencias) / 3

print('Sua media é de: {:.1f}'.format(media))
if media < 5:

    print('-=-' * 5)

    print('Aluno REPROVADO!')

    print('-=-' * 5)

elif media <= 6.9:
    print('-=-' * 5)

    print('Aluno em RECUPERAÇÃO!')

    print('-=-' * 5)
else:


    print('-=-' * 5)

    print('Aluno APROVADO!')

    print('-=-' * 5)