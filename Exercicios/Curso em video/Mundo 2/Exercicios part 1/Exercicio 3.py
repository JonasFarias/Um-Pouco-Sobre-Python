# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais


numero1 = int(input('Digite o PRIMEIRO numero: '))
numero2 = int(input('Digite o SEGUNDO numero: '))

if numero1 > numero2:
    print('O PRIMEIRO tem o valor maior')
elif numero2 > numero1:
    print('O SEGUNDO tem o valor maior')
else:
    print('Os DOIS tem o mesmo valor!')