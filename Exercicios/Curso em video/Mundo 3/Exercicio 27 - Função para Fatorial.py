'''
Crie um programa que tenha uma função fatorial()
que receba dois parâmetros: o primeiro que indique
o número a calcular e outro chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
'''

def fatorial(numero, show=False):
    """
    -> Calcula o fatorial de um numero
    :param numero: Define o valor que vai ser feito o fatorial
    :param show: se True exibe a conta para o fatorial, se False Exibe apenas o resultado
    :return: exibe o fatorial do numero
    """
    from time import sleep
    contador = numero
    fat = 1
    if show == True:
        print(f'Calculando o fatorial de {numero}... ', end=' ')
        while contador > 0:
            print('{} '.format(contador), end=' ')
            print(' X ' if contador > 1 else '', end=' ')
            sleep(0.3)
            fat *= contador
            contador -= 1
        return f' = {fat}'
    else:
        while contador > 0:
            fat *= contador
            contador -= 1
        return f' O fatorial de {numero} é = {fat}'


help(fatorial)

