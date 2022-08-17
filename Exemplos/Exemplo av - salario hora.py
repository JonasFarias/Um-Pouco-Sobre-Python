'''Programa para calcular hora de trabalho!'''

salario = float(input('Valor do Salário: '))
hora_mes = float(input('Hora mês: '))
valor_hora = salario / hora_mes

print(f'O Salário do funcionário é R$ {salario}')
print(f'Total de horas trabalhada mês: {hora_mes}')
print(f'Valor da hora de trabalho R$ {valor_hora}')
