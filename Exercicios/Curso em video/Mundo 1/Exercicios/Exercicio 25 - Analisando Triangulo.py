# Desenvolva um programa que leia o comprimento de três retas e
# diga ao usuário se elas podem ou não formar um triângulo.


numero1 = float(input('Digite um numero: '))
numero2 = float(input('Digite outro numero: '))
numero3 = float(input('Digite mais um numero: '))



if numero1 < numero2 + numero3 and numero2 < numero3 + numero1 and numero3 < numero1 + numero2:
    print('Esses valores podem ser um TRINAGULO')
else:
    print('Esse valor não pode ser um TRIANGULO')