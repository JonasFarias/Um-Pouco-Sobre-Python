#Criar um programa que converta a tempera de |Celsus para fahrenheit

graus = float(input('Quantos graus Cesus esta:'))
conversor = graus * 1.8 + 32

print('A temperatura {}, Celsus, em Fahrenheit é: {}'.format(graus, conversor))