# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros


# INDICE
print('============== LOJAS ==============')
print('\n       FORMAS DE PAGAMENTO\n')
print('===================================')

# RECEBE VALOR DA COMPRA
valor_compra = float(input('Qual o valor da compra R$: '))

# MOSTRA AS OPÇÕES DE PAGAMENTO
print('[1] à vista DINHEIRO 10% de desconto!')
print('[2] à vista DEBITO 05% de desconto!')
print('[3] à vista 2X CARTÃO ')
print('[4] à vista até 6x no CARTÃO: 20% de juros')

# ESCOLHE QUAL A FORMA DE PAGAMENTO
forma_de_pagamento = int(input('Qual vai ser a forma de pagamento: '))
# CALCULA O VALOR DO JUTOS
juros = valor_compra * 20 / 100
# VARIAVEL PARCELA
parcela = 0

# VERIFICA QUAL FOI A FORMA DE PAGAMENTO ESCOLHIDA E APLICA AS REGRAS DE DESCONTO OU JUROS
if forma_de_pagamento == 1:
    print('O valor da compra é R$: {:.2f}, em DINEHEIRO fica R$: {:.2f} '.format(valor_compra, valor_compra - (valor_compra * 10 / 100)))
elif forma_de_pagamento == 2:
    print('O valor da compra é R$: {:.2f}, no DEBITO fica R$: {:.2f}'.format(valor_compra, valor_compra - (valor_compra * 5 / 100)))
elif forma_de_pagamento == 3:
    print('O valor da compra é R$: {:.2f}, em 2X no cartão fica {:.2f}'.format(valor_compra, valor_compra))
elif forma_de_pagamento == 4:
    parcela = int(input('Em quantas vezes você quer fazer: '))
    valor_compra = valor_compra + juros
    print('O valor da compra é R$: {:.2f} com JUROS fica R$: {:.2f}, PARCELADO em {}, a parcela ficará R$: {:.2f}'.format(valor_compra, valor_compra + (juros * parcela), parcela, valor_compra / parcela))












