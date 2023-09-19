


numero = int(input('Digite um numero, para calcular seu fatorial: '))
contador = numero
fatorial = 1
print('Calculando {}! '.format(numero), end=' ')
while contador > 0:
    print('{} '.format(contador), end=' ')
    print(' X ' if contador > 1 else ' ', end=' ')
    fatorial *= contador
    contador -= 1

print('\nO fatorial de {} é {}.'.format(numero,fatorial))