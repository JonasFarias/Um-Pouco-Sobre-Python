# Exercício Python 018: Faça um programa que leia um
# ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.


import math

angulo = int(input('Qual o angulo que deseja:'))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O Angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O Angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O Angulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tangente))
