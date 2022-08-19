#exercicio sobre funções do livro "Curso intensivo de python"

'''8.1 – Mensagem: Escreva uma função chamada display_message() que mostre
uma frase informando a todos o que você está aprendendo neste capítulo. Chame
a função e certifique-se de que a mensagem seja exibida corretamente.


8.2 – Livro favorito: Escreva uma função chamada favorite_book() que aceite
um parâmetro title. A função deve exibir uma mensagem como Um dos meus
livros favoritos é Alice no país das maravilhas. Chame a função e não
se esqueça de incluir o título do livro como argumento na chamada da função.
'''


def display_menssage(mensagem):
    mensagem = 'Estou aprendendo funções no python'
    return mensagem


print(display_menssage(mensagem=''))


meu_livro_favorito = str(input('Seu livro favorito: ')).title()


def livro_favorito(favorito):
    favorito = f'Meu livro Favorito é, {meu_livro_favorito}'
    return favorito

print(livro_favorito(favorito=''))
