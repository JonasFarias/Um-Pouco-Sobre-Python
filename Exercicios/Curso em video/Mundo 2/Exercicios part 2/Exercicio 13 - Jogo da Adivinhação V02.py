#Melhore o jogo do DESAFIO 028 onde o
# computador vai "pensar" em um número entre 0 e 10. Só
# que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
acertou = False
computador = randint(0, 10)
palpites = 0
print('#' * 64)
print('# Sou seu computador acabei de pensar em umnumer entre 0 e 10. #\n# você consegue adivinhar?                                     # ')
print('#' * 64)

while not acertou:
    jogador = int(input('\n\nQual é seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('# ' * 13, end=' ')
            print('\n# Mais tente novamente! #')
            print('# ' * 13, end=' ')
    if jogador > computador:
        print('#' * 26, end=' ')
        print('\n# Menos tente novamente! #')
        print('#' * 26, end=' ')
print('ACERTOU com {}, tentivas!'.format(palpites))


