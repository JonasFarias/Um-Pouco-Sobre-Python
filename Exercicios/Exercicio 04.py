#Faça um programa para escrever a contagem regressiva do lançamento
#de um foguete. O programa deve imprimir 10, 9, 8, ..., 1, 0 e Fogo! na tela.
import time

numero = 11

print('#'*45)
print('#   CONTAGEM REGRESSIVA PARA LANÇAMENTO!    #')
print('#'*45)
while numero !=0:
    time.sleep(1)
    numero -= 1
    print('======= {} '.format(numero))

time.sleep(2)
print('FOGUETE FOI LANÇADO COM SUCESSO!!!')
