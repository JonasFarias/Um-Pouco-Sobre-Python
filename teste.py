'''
filmes = {}

filmes['nome'] = 'filme'
filmes['idade'] = 29
print(filmes['idade'])


alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

carro = {'cor': 'preto', 'portas': 4}
print(carro['cor'])
print(carro['portas'])
'''

produtos = ['carro', 'casa', 'comida', 'litrao']

produto = input('Buscar Prduto: ')
if produto in produtos:
    i = produtos.index(produto)
    print(i)
else:
    print(f'{produto}, não existe na lista!')