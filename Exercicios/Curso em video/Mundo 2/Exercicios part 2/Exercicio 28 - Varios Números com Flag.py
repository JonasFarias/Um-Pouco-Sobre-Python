''' Crie um programa que leia números inteiros
 pelo teclado. O programa só vai parar
  quando o usuário digitar o valor 999,
  que é a condição de parada. No final,
mostre quantos números foram digitados e
qual foi a soma entre elas (desconsiderando o flag). '''



contador = soma = 0
valor = 0
while True:
    soma += valor
    valor = int(input('Digite um valor [999 para PARAR]: '))
    if valor == 999:
        break
    contador += 1
print(f'A soma dos {contador} valores, é de {soma}')
