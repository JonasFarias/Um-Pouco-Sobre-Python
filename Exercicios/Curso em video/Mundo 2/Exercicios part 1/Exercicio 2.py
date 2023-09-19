# Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.



numero = int(input('Digite um numero para ser convertido: '))


print('-=-' * 20)
print('  VOCÊ QUER CONVERTE ESSE NUMERO PARA QUE BASE NUMERICA?')
print('-=-' * 20)


print(' [ 1 ] Converter para BINARIO!')
print(' [ 2 ] Converter para OCTAL!')
print(' [ 3 ] Converter para HEXADECIMAL!')

digito = int(input('Digite uma opção: '))

if digito == 1:
    print('O {} Convertido em BINARIO é: {}'.format(numero, bin(numero)[2:]))
elif digito == 2:
    print('O {} Convertido em OCTAL é: {}'.format(numero, oct(numero)[2:]))
elif digito == 3:
    print('O {} Convertido em HEXADECIMAL é: {}'.format(numero, hex(numero)[2:]))
else:
    print('Desculpa, essa opção é invalida!')


