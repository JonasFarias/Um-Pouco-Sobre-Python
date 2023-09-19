# Desenvolva um programa que leia o nome,
# idade e sexo de 4 pessoas. No final do programa,
# mostre: a média de idade do grupo, qual é o nome do
# homem mais velho e quantas mulheres têm menos de 20 anos.


soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_do_mais_velho =''
mulheres = 0

for c in range(1, 5):
    print('------- PESSOA ------- {}ª'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: '))
    soma_idade += idade
    if c == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_do_mais_velho = nome
    else:
        if idade > maior_idade_homem:
            maior_idade_homem = idade
        if sexo =='Mm' and idade > maior_idade_homem:
            nome_do_mais_velho = nome
    if sexo in 'Ff' and idade <= 20:
        mulheres += 1



print('Tem {} mulheres menores de idade'.format(mulheres))
media_idade = soma_idade / 4

print('A media de idade é {}'.format(media_idade))
print('O homem mais velho é {} com a idade {}'.format(nome_do_mais_velho, maior_idade_homem))