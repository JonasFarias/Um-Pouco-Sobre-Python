'''Crie um programa que leia vários números inteiros pelo
teclado. O programa só vai parar quando o usuário digitar o
valor 999, que é a condição de parada. No final, mostre quantos
números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

valor = 0
soma = 0
contador = 0
while valor != 999:
    soma += valor
    contador += 1
    valor = int(input('Digite um valor [999 Para Encerrar]: '))

print('Você digitou {} numeros e a soma desses numeros é de {}'.format(contador, soma))
