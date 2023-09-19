'''Crie um programa onde o usuário
possa digitar vários valores numéricos
e cadastre-os em uma lista. Caso o número
já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os
valores únicos digitados, em ordem crescente.'''

valores = []

while True:
    valor = (int(input('Digite um Valor: ')))
    if valor not in valores:
        valores.append(valor)
        print('Valor Adicionado com Sucesso!')
    else:
        print('Valor Dupliado! Não vou adicionar! ')
    resposta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resposta in 'N':
        break
valores.sort()
print(f'Os valores digitados foram {valores}')
print('ACABOU!')


