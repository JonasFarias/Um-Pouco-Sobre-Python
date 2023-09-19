# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 parta viagens mais longas.




distancia = float(input('Qual a distancia da viagem!'))
taxa_viagem = 0.5 * distancia
taxa_promocional = 0.45 * distancia

if distancia <= 200:
   print('O valor da viagem vai ser de: {}'.format(taxa_viagem))
else:
    print('O valor da viagem vai ser de: {}'.format(taxa_promocional))