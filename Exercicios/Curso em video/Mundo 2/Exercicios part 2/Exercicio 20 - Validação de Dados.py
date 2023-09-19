#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso
# esteja errado, peça a digitação novamente até ter um valor correto.



sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('Dado invalido, por favor informe seu sexo [M/F]: ')).strip().upper()[0]
print('Obrigado, sexo registrado com sucesso!')