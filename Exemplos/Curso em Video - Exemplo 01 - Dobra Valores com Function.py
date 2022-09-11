def dobra_valores(lst):
    """

    :param lst:
    :return:
    """
    posicao = 0
    while posicao < len(lst):
        lst[posicao] *= 2
        posicao +=1


valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(valores)
dobra_valores(valores)
print(f'{valores}')

