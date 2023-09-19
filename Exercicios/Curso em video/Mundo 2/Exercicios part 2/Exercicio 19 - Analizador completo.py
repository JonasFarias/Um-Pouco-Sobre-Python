# Desenvolva um programa que leia o nome,
# idade e sexo de 4 pessoas. No final do programa,
# mostre: a média de idade do grupo, qual é o nome do
# homem mais velho e quantas mulheres têm menos de 20 anos.

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomehomemaisvelho = ''
totmulher20 = 0
for pessoas in range (1, 5):
    print('------ {}ª ------'.format(pessoas))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade

    if pessoas == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomehomemaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomehomemaisvelho = nome
    if sexo in 'Ff' and idade <20:
        totmulher20 += 1

mediaidade = somaidade / 4
print('Á média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho se chama {} e a idade é: {}'.format(nomehomemaisvelho, maioridadehomem))
print('São {} mulheres com idade menor que 20.'.format(totmulher20))



