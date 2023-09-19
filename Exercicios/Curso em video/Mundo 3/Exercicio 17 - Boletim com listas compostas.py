'''Exercício Python 089: Crie um programa que leia nome e
duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e
permita que o usuário possa mostrar as notas de cada aluno individualmente.'''


ficha_aluno = []
alunos = []
while True:
    nome = str(input('Nome do Aluno: ')).upper()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha_aluno.append([nome, [nota1, nota2], [media]])
    escolha = str(input('Quer continuar [S/N] ')).strip().upper()[0]
    if escolha == 'N':break
print('-=' * 10, 'BOLETIM', '-=' * 10)

print('=' * 30)
print(f'{"Nº.":<4}{"NOME: ":<10}{"MÉDIA":>8}')
for indice, aluno in enumerate(ficha_aluno):
    print(f'{indice+1:<4}{aluno[0]:<10}{media:8.1f}')
print('=' * 30)

while True:
    print('=' * 30)
    opcao = int(input('Nota de que alunos você quer ver [999] para ENCERRAR: '))
    if opcao == 999:
        print('FINALIZANDO...')
        break
    if opcao <= len(ficha_aluno) -1:
        print(f'Notas de {ficha_aluno[opcao][0]} São {ficha_aluno[opcao][1]}')
print('VOLTE SEMPRE!')

