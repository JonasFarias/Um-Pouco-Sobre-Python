#Desenvolva um  programa que leia o primeiro
# termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.



print('===' * 10)
print('   10 TERMOS  DE UMA PA')
print('===' * 10)


primeiro_termo = int(input('\nQual o primeiro termo: '))
razao = int(input('Qual a razao: '))
decimo = primeiro_termo + (10 - 1) * razao
for c in range(primeiro_termo, decimo + razao, razao):
    print('{} ->  '.format(c), end='')
print('ACABOU')