'''Escreva uma expressão para determinar se uma pessoa deve ou não
pagar imposto. Considere que pagam imposto pessoas cujo salário é maior que
R$ 1.200,00.'''

salario = int(input('Olá vamos ver se você tem que pagar impostos? Digite seu salário: '))

if salario <= 1200:
    print('Não você não precisa pagar imposto!')
else:
    print('Sim você tem que pagar imposto!')
