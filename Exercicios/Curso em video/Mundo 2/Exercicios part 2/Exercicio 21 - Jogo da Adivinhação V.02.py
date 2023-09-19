#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar”
# em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.


from random import randint
computador = randint(0, 10)
placar = 1
print('Oi sou seu computador, e vou jogar um jogo com você, eu pensei em numero tente adivinhar!')
jogador = int(input('Eai qual numero eu pensei? '))

while computador != jogador:
    placar += 1
    if computador < jogador:
        print('Hmmmm.... Menos')
    elif computador > jogador:
        print('Mais....')
    jogador = (int(input('Tente novamente: : ')))

print('#' * 65)
print('Isso eu pensei no {}.'.format(computador))
print('Ganhou, você precisou de {} tentativas. Obrigado por jogar!'.format(placar))
print('#' * 65)


