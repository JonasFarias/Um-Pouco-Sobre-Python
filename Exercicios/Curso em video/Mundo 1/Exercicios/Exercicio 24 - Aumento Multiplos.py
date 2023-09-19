# Escreva um programa que pergunte o salário de um funcionário e
# calcule o valor do seu aumento. Para salários superiores
# a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.


salario = float(input('Qual o valor do salário R$: '))

aumento1 = salario + (salario * 15) / 100
aumento2 = salario + (salario * 10) / 100

if salario <= 1250:
    print('O seu salario a partir de agora é R$: {}'.format(aumento1))
else:
    print('O seu salario a partir de agora é R$: {}'.format(aumento2))

