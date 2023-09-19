# Faça um programa que leia o comprimento do cateto
# oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

import math

cateto_oposto = float(input('Qual o compirmento do Cateto Oposto:'))
cateto_adjecente = float(input('Qual o comprimento do Cateto Adjecente:'))
hipotenusa = math.hypot(cateto_oposto, cateto_adjecente)

print('O valor da hipotenusa é: {:.2f}'.format(hipotenusa))