# Crie um programa que leia um valor em metro e converta para centimetro e milimitro


numero = float(input('Digite um valor:'))

cm = numero * 100
mm = numero * 1000


print('Convertendo o valor de {} metros, para: \n CM {:.0f} \n MM {:.0f}'.format(numero, cm, mm))
