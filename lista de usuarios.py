
usuarios = ['Jonas', 'Eick', 'Marcelo', 'Admin', 'George', 'Maria']

login = str(input('Usuario : '))

if login in usuarios:
    if login == 'Admin':
        print(f'Olá, {login}, gostaria de ver um relatorio?')
    else:
        print(f'Olá, {login} seja bem vindo!')

