'''
Crie um programa que tenha a função leiaInt(),
que vai funcionar de forma semelhante ‘a função input() do Python,
só que fazendo a validação para aceitar apenas um valor
numérico. Ex: n = leiaInt(‘Digite um n: ‘)
'''
# Função para subistituir o input com uma validação
def LeiaInt(msg):
    """
    -> Função para substituir o input com uuma validação se o numero é valido ou não
    :param msg: Recebe uma mensagem
    :return: retorna o valor
    """
    ok = False
    valor = 0

    while True:
        #vai receber a mensagem do input
        n = str(input(msg))
        # se o que for difitado for um numero, ele valida o ok
        if n.isnumeric():
            # se for um numero o valor deixa de ser 0 e recebe o valor digitado
            valor = int(n)
            # variavel ok se torna verdadeira
            ok = True
        # se não for um numero que foi digitado ele vai ficar exibindo a mensagem de erro na cor vermelha
        else:
            print('\033[0;31mERRO! Digite um numero valigo\033[m')
        # se estiver tudo ok, o while para
        if ok:
            break
    # retorna o valor
    return valor
#faz a leitura do que foi digitaado
num = LeiaInt('Digite um numero')
#se for um numero é exibido essa mensagem
print(f'Você acabou de digitar {num}')

