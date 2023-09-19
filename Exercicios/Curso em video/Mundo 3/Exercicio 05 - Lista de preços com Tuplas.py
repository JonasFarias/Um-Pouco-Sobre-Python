'''Crie um programa que tenha uma tupla única
com nomes de produtos e seus respectivos
preços, na sequência. No final, mostre uma
listagem de preços, organizando os dados em forma tabular.'''

#TUPLA COM, UMA LISTA DE PRODUTOS E SEUS VALORES
listagem = ('Teclado', 75,
            'Mouse', 14.90,
            'HD 500 GB', 110,
            'Gabinete', 329,
            'Fonte', 150,
            'Memoria Ram 500 GB', 99)

#formatação do titulo
print('-' * 40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-' * 40)

#PARA CADA POSIÇÃO NO RANGE DE 0 ATÉ O TAMANHO TOTAL DA LISTAGEM
#Vai verificar se a posição for par, se for ele vai printar formatado
#Se não vai printar os preços formatados
for posicao in range(0, len(listagem)):
    if posicao % 2 == 0:
        #printa a lista formatada
        print(f'{listagem[posicao]:.<30}', end='')

    else:
        #printa os preços formatados
        print(f'R$: {listagem[posicao]:>7.2f}')
print('-' * 40)


