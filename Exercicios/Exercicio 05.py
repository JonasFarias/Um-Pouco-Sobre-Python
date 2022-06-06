#Altere o programa anterior para exibir os resultados 
#no mesmo formato de uma tabuada: 2x1 = 2, 2x2=4, ...



contador = 1
numero = int(input('qual tabuada você quer saber: '))
print('{} X {} = {}'.format(numero, 1, numero * 1))
while contador < 10:
    contador += 1
    resultado = numero * contador

    print('{} X {} = {}'.format(numero,contador, resultado))

