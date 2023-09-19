'''Crie um programa que simule o
funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''


print('=' * 20)
print('       BANCO')
print('=' * 20)

valor_saque = int(input('Valor a sacar R$: '))
cedula = 50
valor = valor_saque
total_cedulas = 0
while True:
    if valor >= cedula:
        valor -= cedula
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Total de {total_cedulas},cedulas  de R$:{cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        if valor == 0:
            break

print('=' * 20)
print('{:^20}'.format('BANCO'))
print('=' * 20)
