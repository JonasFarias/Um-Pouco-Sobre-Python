'''
Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai retornar
um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)
'''

def notas(*nota, situacao=False):
    """
    -> Função para receber notas e avaliar a situação do alunmo
    :param nota: Recebe varias notas e mostra
    :param situacao: se situação for True exibe as seguintes msg Ruim,Regular ou Boa!
    :return: retorna a nota
    """
    notas = dict()
    notas['total'] = len(nota)
    notas['maior'] = max(nota)
    notas['menor'] = min(nota)
    notas['media'] = sum(nota)/len(nota)
    if situacao == True:
        if notas['media'] <= 5:
            return f'{notas} Situação RUIM!'
        elif notas['media'] <= 7:
            return f'{notas} Situação REGULAR!'
        else:
            return f'{notas} Situação BOA'

    return notas

sala = notas(5.5, 6.7, 1, 1, 6, 7.3, 10, 1, situacao=True)
print(sala)
