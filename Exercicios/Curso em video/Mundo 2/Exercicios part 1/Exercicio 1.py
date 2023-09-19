# Escreva um programa para aprovar o empréstimo
# bancário para a compra de uma casa. Pergunte
# o valor da casa, o salário do comprador e em
# quantos anos ele vai pagar. A prestação mensal
# não pode exceder 30% do salário ou então o empréstimo será negado.


# RECEBE OS VALORES
casa = float(input('Valor casa: '))
parcelas = int(input('Quantidade parcelas'))
salario = float(input('Qual seu salario'))
prestacao = casa / (parcelas * 12) # DIVIDE A QUANTIDADE DE ANOS EM MESES
minimo = salario * 30 / 100 # CALCULA A PORCENTAGEM MINIMA QUE TEM QUE SER PAGA

print('Para pagar uma casa de R$: {:.2f} em {} anos'.format(casa, parcelas), end='')
print(' a prestação será de R$: {}'.format(prestacao))


# CHECA SE O SALARIO É SUFICIENTE PARA PAGAR AS PARCELAS, SE SUFICIENTE O EMPRESTIMO É LIBERADO, SE NÃO FOR EMPRESTIMO NEGADO
if prestacao <= minimo:
    print(('Emprestimo APROVADO!'))
else:
    print('Emprestimo NEGADO!')

