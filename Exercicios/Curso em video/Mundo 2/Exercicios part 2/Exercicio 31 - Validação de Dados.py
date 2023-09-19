'''Crie um programa que leia a idade
e o sexo de várias pessoas. A cada pessoa cadastrada, o
programa deverá perguntar se o
usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''


print('=' * 20)
print('CADASTRE UMA PESSOA!')
print('=' * 20)

total_pessoas_maiores = 0
mulheres_menores = 0
total_homens = 0
sexo = ''
while True:
    idade = int(input('Idade: '))
    if idade >= 18:
        total_pessoas_maiores += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if sexo == 'M':
            total_homens += 1
        elif sexo == 'F' and idade < 18:
            mulheres_menores += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break

print(f'Total de PESSOAS maiores é de {total_pessoas_maiores}')
print(f'Total de HOMENS cadastrado foi de {total_homens}')
print(f'Total de MULHERES menores é de {mulheres_menores}')



