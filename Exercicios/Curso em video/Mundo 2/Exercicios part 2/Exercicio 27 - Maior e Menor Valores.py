'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre
todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores.'''




validacao = 'Ss'
soma = 0
contador = 0
maior = 0
menor = 0
while validacao not in 'Nn':
    valor = int(input('Digite um numero: '))
    validacao = str(input('Quer continuar Sim ou Não: ')).strip().upper()[0]
    contador += 1
    soma = soma + valor
    if contador == 1:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

media = soma / contador
print('Você Digitou {} e a media foi de {}'.format(contador, media))
print('O maior numero foi {} e o menor foi {}'.format(maior, menor))
print('FIM')
