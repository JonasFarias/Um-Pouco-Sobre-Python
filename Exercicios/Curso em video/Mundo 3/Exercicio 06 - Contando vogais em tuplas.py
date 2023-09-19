'''Crie um programa que tenha uma tupla com várias palavras
(não usar acentos).
Depois disso, você deve mostrar,
para cada palavra, quais são as suas vogais.'''

palavras = ('casa', 'janela', 'banheiro', 'python', 'comida',
           'escola', 'trabalho', 'dinheiro')

for palavra in palavras:
    print(f'\n Na palavra {palavra.upper()} temos - ', end='')
    for letras in palavra:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')