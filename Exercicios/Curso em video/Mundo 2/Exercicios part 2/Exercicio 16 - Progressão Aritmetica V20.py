'''Refaça o DESAFIO 051, lendo o primeiro termo e
a razão de uma PA, mostrando os 10 primeiros termos da
progressão usando a estrutura  while.'''


print('===' * 10)
print('   10 TERMOS  DE UMA PA')
print('===' * 10)

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
contador = 1
while contador <= 10:
    print('{} ->'.format(termo), end='')
    termo += razao
    contador += 1
print('FIM')