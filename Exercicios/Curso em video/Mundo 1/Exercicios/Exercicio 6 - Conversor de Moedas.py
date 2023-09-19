# Crie um programa que converta real em dolar


real = float(input('Quanto em real você quer converter em dolar:'))

dolar = real / 5.44

print('você converteu R$:{:.2f}, em US$:{:.2f} doláres'.format(real, dolar))