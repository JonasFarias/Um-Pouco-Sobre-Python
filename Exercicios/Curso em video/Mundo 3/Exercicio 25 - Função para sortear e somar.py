'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia()
e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista
e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''

#Importa a função para randomizar o sorteio
from random import randint
#Importa a função para o delay da impressão
from time import sleep

#função para sortear
def sorteio(lista):
    print('Sorteando os numeros:', end=' ')
    contador = 1
    #Enquanto o contador for menor que 5 ele vai adicionar um numero a lista de 5 numeros
    while contador <= 5:
        #randomiza um valor de 1 a 10
        numero = randint(1, 10)
        #adiciona o numero sorteado a lista
        numeros.append(numero)
        #soma o contador para chegar a 5
        contador += 1
    #para cada numero da lista ee printa o numero
    for num in numeros:
        print(f'{num}', end=' ')
        sleep(0.3)
    print('PRONTO!')

#soma os valores pares da lista
def somaPar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'\nA soma dos pares da lista{lista} é de {soma}')



numeros = []
sorteio(numeros)
somaPar(numeros)