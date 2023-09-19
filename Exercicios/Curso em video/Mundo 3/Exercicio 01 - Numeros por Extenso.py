'''Crie um programa que tenha uma dupla totalmente preenchida
com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um
 número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

#Tupla, com valores de zero a vinte!
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
           'Desesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

#looping infinito,
while True:
    #Pede para o usuario, digitar um numero entre zero a vinte
    numero = int(input('Escolha um numero de 0 a 20: '))
    #verifica se o numero digitado esta dentro de zero a vinte
    if 0 <= numero <= 20:
        #para o programa
        break

        #só impreme se o valor não for correspondente
    print('Valor Invalido, tente novamente', end=' ')
#impreze o indice da tupla de 0 a vinte
print(f'Você Digitou o {extenso[numero]}')