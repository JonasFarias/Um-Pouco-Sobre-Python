"""Escreva um programa que leia dois números e que pergunte qual
operação você deseja realizar. Você deve poder calcular a soma (+), subtração (-),
multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada
"""
number1 = float(input('Digite um numero: '))
number2 = float(input('Digite outro numero: '))

print('O QUE DESEJA FAZER? ')
print('1 SOMAR')
print('2 SUBTRAIR')
print('3 DIVIDIR')
print('4 MULTIPLICAR')
operacao = int(input('ESCOLHA UMA OPÇÃO: '))

if operacao == 1:
    print('A Soma do numero: {}, e do numero {} é de {}.'.format(number1, number2, (number1 + number2)))
if operacao == 2:
    print('A SUBITRAÇÃO DO NUMERO {}, E DO NUMERO {}, É DE: {}'.format(number1,number2, (number1 - number2)))
