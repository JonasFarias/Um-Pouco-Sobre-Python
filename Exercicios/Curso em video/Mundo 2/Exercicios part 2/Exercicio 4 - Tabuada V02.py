#Refaça o DESAFIO 009, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.

tabuada = int(input('Digite um numero queira saber a tabuada'))
contador = 0

print(' # ' * 6)
for c in range (1, 11):
    contador = contador + 1
    print('    {} X {} = {}'.format(tabuada, contador, tabuada * contador ))

print(' # ' * 6)
print('\nSua TABUADA')