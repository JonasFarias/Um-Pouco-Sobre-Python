#faça um programa que leia a largura x altura de uma parede e calcule quanto de tinra ele precisa usar
#considerando que cada litro de tinra pinta 2m²


largura = float(input('Qual a largura da sua parede:'))
altura = float(input('Qual a altura da sua parede'))
metro_quadrado = largura * altura

print('Sua parede tem a dimensãp de {}X{} com um total de {}m²'.format(largura,altura, largura * altura))
print('Para pintar essa parede você vai precisar de {}lt de tinta'.format(metro_quadrado / 2))