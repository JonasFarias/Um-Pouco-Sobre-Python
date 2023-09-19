# Crie um programa que pegue um numero e de seu antessesor e sua sucessor


'''Recebe um dado digitado pelo usuario'''
numero = int(input('Digite um valor:'))


''' Exibe o dado digitado, calcula o antessessor e o sucessor'''
print('Analisando o valor: {}, o seu antessessor é: {}, e o seu sucessor é: {}'.format(numero, (numero - 1), (numero + 1)))