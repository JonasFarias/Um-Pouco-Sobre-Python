'''Faça um programa que leia 5 valores numéricos e
guarde-os em uma lista.
No final, mostre qual foi o
maior e o menor valor digitado e as
suas respectivas posições na lista.'''

valores = []
for contador in range(0, 5):
    valores.append(int(input(f'Digite um valor para posição {contador}: ')))
print('=-=' * 20)
print(f'O maior valor digitado foi {max(valores)}, na posição', end='')
for indice, valor in enumerate(valores):
    if valor == max(valores):
        print(f' {indice}...', end='')
print()
print(f'O menor valor digitadoo foi {min(valores)}, na posição', end='')
for indice, valor in enumerate(valores):
    if valor == min(valores):
        print(f' {indice}...', end='')
print()
print('=-=' * 20)
print('ACABOU!')
