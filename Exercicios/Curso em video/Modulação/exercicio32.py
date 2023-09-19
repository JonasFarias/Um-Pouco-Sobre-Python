'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas
aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.
'''

def aumentar(numero, formato=False):
    porcentagem = numero * 0.1
    aumento = numero + porcentagem
    return aumento if formato False


def diminuir(numero):
    porcentagem = numero * 0.1
    menos = numero - porcentagem
    return menos

def dobro (numero):
    dobrar = numero * 2
    return dobrar

def metade(numero):
    metade = numero / 2
    return metade

def moeda(numero):
    texto = f'R$ {numero:.2f}'.replace('.', ',')
    return texto

def resumo(numero):
    texto = len('resumo')
    print('=' * texto)
    print('resumo')
    print('=' * texto)

    print((f'O dobro de {numero}, é de {dobro(numero)}'))
    print(f'A metade de {numero}, é de : {metade(numero)}')

    print('=' * texto)