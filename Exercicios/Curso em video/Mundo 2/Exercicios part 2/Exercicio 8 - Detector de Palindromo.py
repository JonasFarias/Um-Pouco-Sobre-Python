# Crie um programa que leia uma frase qualquer e
# diga se ela é um palíndromo, desconsiderando os espaços.

# lê a frase
frase = str(input('Digite muma frase: ')).strip().upper()
# tira os espaços em branco e cria uma lista
palavras = frase.split()
# junta os blocos, para a frase ficar juntos
junto = ''.join(palavras)
# contador para inverter
inverso = ''

# inverte a lista, vai da ultima letra até a primeira, voltanod uma letra
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]

#verifica se o inverso é iual, se for ele mostra
if inverso == junto:
    print('Temos um palíndromo!')

# se não for ele mostra
else:
    print('A frase digitada não é um palíndromo!')