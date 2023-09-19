#faça um algorismo que calcule o desconte de um produto

produto = float(input('Qual o valor do produto:'))
desconto = int(input('Qual o valor do desconto:'))
valor_do_desconto = produto * desconto / 100
valor_atualizaado = produto - valor_do_desconto

print('O produto que custava RS:{}, com o desconto de {}%, custará R$:{}. \n Boa compra!'.format(produto, desconto, valor_atualizaado))