# faça um algoritimo que mostre o salario de um
# funcionario e o novo salario com aumento de 15%

salario = float(input('Qual o valor do salário:'))
aumento = salario * 15 /100
salario_novo = salario + aumento
print('O Seu salário era de R$:{}, agora teve o reajuste de 15% e o seu salário vai passar a ser R$:{:.2f}'.format(salario,salario_novo))