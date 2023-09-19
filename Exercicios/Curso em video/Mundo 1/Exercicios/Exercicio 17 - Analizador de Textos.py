# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo:')).strip()
# colocando.strip ele ja deixa o nome cortado, removendo os espaços assim a contagem não contara
# com os esoaços vazios)
nome_maiusculo = nome.upper()

nome_minusculo = nome.lower()
primeiro_nome = nome.find(' ')
    #procura o primeiro espaço e conta e conta quantas letras tem antes dele

print('Ao todo seu nome tem {} de letras'.format(len(nome) - nome.count(' ')))
        # -nome.count(' ') vai contar todos os espaços e eliminar eles
print('Em Maiusculo: {}'.format(nome_maiusculo))
        # transforma seu nome em maiusculo
print('Em minusculo: {}'.format(nome_minusculo))
        # transforma seu nome em minusculo
print('Seu primeiro nome tem: {} letras.'.format(primeiro_nome))
        # exibe seu primeiro nome