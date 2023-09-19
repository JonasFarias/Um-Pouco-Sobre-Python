'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

soma_pares = maior_numero = soma_coluna = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range (0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um numero para [{linha},{coluna}]: '))

print('=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]



    print()
print('=' * 30)
print(f'A soma dos numeros pares é de: {soma_pares}')
for linha in range(0, 3):
    soma_coluna += matriz[linha][2]
print(f'A soma da Terceira Coluna da Matriz é de: {soma_coluna}')
for coluna in range(0, 3):
    if coluna == 0:
        maior_numero = matriz[1][coluna]
    elif matriz[1][coluna] > maior_numero:
        maior_numero = matriz[1][coluna]
print(f'O maior numero da segunda linha é: {maior_numero}')
