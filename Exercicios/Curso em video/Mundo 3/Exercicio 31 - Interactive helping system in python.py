'''
Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
'''

c = ('\033[m',         # 0 - Sem cor
     '\033[0;30;41m',  # 1 - Vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelho
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[7;30m'      # 6 - branco
);


def Ajuda(com):
    print(c[5], end='')
    help(com)
    print(c[5], end='')


def Titulo(msg, cor=0):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


#programa principal
comando =''
while True:
    Titulo('SISTEMA DE AJUDA PyHelp', 1)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        Ajuda(comando)
Titulo('ATÉ LOGO')

