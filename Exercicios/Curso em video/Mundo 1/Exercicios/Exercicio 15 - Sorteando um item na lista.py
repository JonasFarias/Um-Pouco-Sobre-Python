# Um professor quer sortear um dos seus quatro
# alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

aluno_1 = str(input('Insira o nome do aluno:'))
aluno_2 = str(input('Insira o nome do proximo aluno:'))
aluno_3 = str(input('Insira o nome do proximo aluno'))
aluno_4 = str(input('Insira o nome do ultimo aluno'))

lista = [aluno_1, aluno_2, aluno_3, aluno_4]

sorteio = random.choice(lista)

print('Parabéns, o aluno sorteado é {}'.format(sorteio))