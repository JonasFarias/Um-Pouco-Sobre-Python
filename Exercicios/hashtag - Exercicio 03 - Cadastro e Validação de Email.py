'''"""## 3. Cadastro de e-mails
- liragmail.com NÃO é um e-mail válido
- lira@gmail NÃO é um e-mail válido
- lira@gmail.com é um e-mail válido
Crie um programa que permita o cadastro de nome e e-mail
de uma pessoa (por meio de inputs) e que verifique:
1. Se nome e e-mail foram preenchidos, caso contrário
ele deve avisar para preencher todos os dados corretamente
2. Se o e-mail contém '@' e se depois do '@' existe algum '.',
caso contrário ele deve exibir uma mensagem de e-mail inválido
Obs: Pode te ajudar lembrar do método .find da aula de Métodos de String.
Você pode testar o que ele dá como resposta caso ele não encontre um item dentro da string
"""'''


nome = input('Nome: ')
email = input('Email: ')

if nome and email:
    posicao_arroba = email.find('@')
    servidor = email[posicao_arroba:]
    if posicao_arroba != -1 and '.' in servidor:
        print('Cadastro Concluido!')
    else:
        print('e-mail invalido! ')
else:
    print('Digite seu nome e email corretamente! ')
