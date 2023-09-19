'''Crie um programa onde o
usuário possa digitar cinco valores
numéricos e cadastre-os em uma lista,
já na posição correta de
inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.'''

valores = []
for contador in range(0, 5):
    numero = int(input('Digite um valor: '))
    if contador == 0 or numero > valores[-1]:
        valores.append(numero)
    else:
        posicao = 0
        while posicao < len(valores):
            if numero <= valores[posicao]:
                valores.insert(posicao, numero)
                break
            posicao += 1
print('=-=' * 20)
print(f'Os valores digitados foram {valores}')
