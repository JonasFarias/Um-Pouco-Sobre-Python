'''Crie uma function que calcule qual o %
de carga tributária que está sendo aplicado
sobre um determinado produto, dado o preço de venda,
o "lucro" e os custos (com exceção do imposto) dele.
preco = 1500
custo = 400
lucro = 800

'''

preco = 1500
custo = 400
lucro = 800


def carca_tributaria(preco, custo, lucro):
    imposto = preco - custo - lucro
    return imposto / preco

print(f'A carga tributaria foi de {carca_tributaria(preco, custo, lucro):.1%}')

