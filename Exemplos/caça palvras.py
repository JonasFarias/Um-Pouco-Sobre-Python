
def filtrar_palavra(lista, pedaço_palavra):
    palavra_filtrada = []
    for letra in lista:
        if pedaço_palavra in letra:
            palavra_filtrada.append(letra)
    return palavra_filtrada


palavras = ['casas', 'coisa', 'ordem', 'quero', 'poste']

palavra = filtrar_palavra(palavras, 'ue')
print(palavra)
