# Desenvolva um programa que leia seis
# números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado
# for ímpar, desconsidere-o.


soma = 0
for c in range (1, 7):
    numero = int(input(' Digite um numero: '))
    if numero % 2 == 0:
        soma = soma + numero
print('A soma dos numeros pares que voê digitou é: {}'.format(soma))

