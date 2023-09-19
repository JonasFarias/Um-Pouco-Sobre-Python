'''
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os
dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''

grupo = []
cadastro = {}
soma = media = 0
while True:
    cadastro.clear()
    cadastro['nome'] = str(input('Nome: ')).upper()
    while True:
        cadastro['sexo'] = str(input('Sexo [M/F]: ').upper()[0])
        if cadastro['sexo'] in 'MF':
            break
        print('ERRO, Digite somente M ou F')
    cadastro['idade'] = int(input('Idade:'))
    soma += cadastro['idade']
    grupo.append(cadastro.copy())
    while True:
        resposta = str(input('Deseja Continuar [S/N]: ')).upper()[0]
        if resposta in 'SN':
            break
        print('Erro, Digite Apenas S ou N')
    if resposta == 'N':
        break
print('=-=' * 30)
print(f'A) Ao todo temos {len(grupo)} pessoas cadastrada!')
media = soma / len(grupo)
print(f'B) média de idade é {media:5.2f} anos')
print(f'C) As Mulheres Cadastradas foram', end=' ')
for mulher in grupo:
    if mulher['sexo'] in 'F':
        print(f'{mulher["nome"]}', end=' ')
print()
print(f'D) Lista de pessoas  que estão acima da média: ', end=' ')
for pessoa in grupo:
    if pessoa['idade'] >= media:
        print(' ', end=' ')
        for chave, valor in pessoa.items():
            print(f' {chave} = {valor}', end=' ')
        print()
print('ENCERRADO')

