#Crie um programa que leia o ano de nascimento de sete pessoas. No final,
#mostre quantas pessoas ainda não
#atingiram a maioridade e quantas já são maiores.
'''
primeiro programa que eu fiz depois de um ano sem praticar, não lembrava como
 fazia então fiz dessa maneira


maior = 0
menor = 0
contador = 0

while contador < 7:
    idade =  int(input('Digite sua idade: '))
    contador = contador + 1
    if idade < 18:
        menor = menor + 1
    elif idade >= 18:
        maior = maior +1

print('{}, são menores de idade e {} são maiores de idade'.format(menor,maior))
'''

'''AGORA FAZENDO DO JEITO QUE DEVERIA SER:'''

from datetime import date


data_atual = date.today().year
maior = 0
menor = 0
for pessoa in range(1, 8):
    ano_nascimento = int(input('Qual o ano de nascimento da {}º pessoa: '.format(pessoa)))
    idade = data_atual - ano_nascimento

    if idade < 18:
        menor = menor + 1
    elif idade >= 18:
        maior += 1

print('Temos {}, pessoas maiores de idade, e também temos {}, menores de idade!'.format(maior, menor))