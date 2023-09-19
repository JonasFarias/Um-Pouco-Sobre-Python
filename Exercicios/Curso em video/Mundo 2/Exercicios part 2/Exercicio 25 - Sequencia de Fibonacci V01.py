'''Escreva um programa que leia um número N
inteiro qualquer e mostre na tela os N
primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8'''


# Exibe o nome, é só uma firula
print('#' * 30)
print('SEQUENCIA DE FIBONACCI V01')
print('#' * 30)
# pergunta ao usuario quantos termos ele quer mostrar!
sequencia = int(input('Quantos termos você quer mostrar? '))
#primeiro termo da sequencia de fibonacci sempre é zero
termo1 = 0
#segundo termo da sequencia de fibonacci sempre é um por tanto já deixamos definidos
termo2 = 1

#impreme o termo 1 e termo 2 exibindo na tela seus valores
print('~'*30)
print('{} - {}'.format(termo1, termo2), end='')
''' o contador inicia no três porque já definimos o termo 1 e o termo 2 então precisamos
 que o programa comece a contar depois do segundo termo'''
contador = 3

'''enquanto o contator for menor que a sequencia que o usuario pediu ele vai somar os termos criando 
#o termo 3'''
while contador <= sequencia:
    #somando os termos
    termo3 = termo1 + termo2
    #imprimindo o terceiro termo
    print(' - {}'.format(termo3), end='')

    '''agora precisamos que os termos sejam subistituidos para que a soma seja feita
    por isso o termo 1 recebe o valor do termo 2 e o termo 2 recebe o valor do termo 3
    até o final da sequencia desejada'''
    termo1 = termo2
    termo2 = termo3
    # comamos o contator
    contador += 1

    #fim
print(' - FIM ')
print('~'*30)
