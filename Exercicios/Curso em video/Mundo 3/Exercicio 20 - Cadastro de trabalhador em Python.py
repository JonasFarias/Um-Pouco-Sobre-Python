'''
Crie um programa que leia nome, ano de nascimento e carteira de
trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário
receberá também o ano de contratação e o salário. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar
'''
from datetime import date
trabalhador = {}

trabalhador['nome'] = str(input('Nome: '))
trabalhador['ano_nascimento'] = int(input('Ano do Nascimento: '))
trabalhador['ctps'] = int(input('CTPS: '))

if trabalhador['ctps'] <= 0:
    print('-=' * 30)
    print(f'Nome: {trabalhador["nome"]}')
    idade = date.today().year - trabalhador['ano_nascimento']
    print(f'Idade: {idade}')
    print(f'CTPS tem valor: {trabalhador["ctps"]}')
else:
    trabalhador['salario'] = float(input('Salário: '))
    trabalhador['ano_contratacao'] = int(input('Ano de contratação: '))
    tempo_trabalhado = date.today().year - trabalhador['ano_contratacao']
    print('=-' * 30)
    print(f'Nome: {trabalhador["nome"]}')
    idade = date.today().year - trabalhador['ano_nascimento']
    aposentadoria = trabalhador['idade'] + ((trabalhador['ano_contratacao'] + 35) - date.today().year)
    print(f'Idade: {idade}')
    print(f'CTPS: {trabalhador["ctps"]}')
    print(f'Salário: {trabalhador["salario"]}')
    print(f'Vai se aposentar com {aposentadoria} anos')


#lembrete que vou ter que vim corrigir a logica da aposentadoria por hora preguiça!