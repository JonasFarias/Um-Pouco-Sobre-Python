# Escreva um programa que pergunte a quantidade de
# Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.




dias = int(input('Quantos dias alugado:'))
km = float(input('Quantos Km você percorreu:'))
aluguel_diarias = 60 * dias
aluguel_km_rodados = 0.15 * km

total_a_pagar = aluguel_diarias + aluguel_km_rodados

print('O valor a ser pago é de {}'.format(total_a_pagar))