'''Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário. No final,
mostre o conteúdo da estrutura na tela.'''

aluno = {}
nome_aluno = str(input('Nome: '))
media = float(input('Media: '))
aluno['nome_aluno'] = nome_aluno
aluno['media'] = media

if media <= 4:
    print(f'O aluno, {aluno["nome_aluno"]}')
    print(f'Foi REPROVADO com a media:  {aluno["media"]}.')
if media <= 6:
    print(f'O aluno, {aluno["nome_aluno"]}')
    print(f'Ficou de RECUPERAÇÃO com a media: {aluno["media"]}')
if media <= 9:
    print(f'O aluno, {aluno["nome_aluno"]}')
    print(f'Foi APROVADO com a nota! {aluno["Media"]}. ')
if media == 10:
    print(f'O aluno, {aluno["nome_aluno"]}')
    print(f'Foi APROVADO com a nota MAXIMA {aluno["media"]}')
