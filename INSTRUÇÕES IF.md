# IF(SE)


O tipo mais comum de instrução de controle de fluxo é a instrução `if`.
Uma instrução `if` pode ser lida como “se (if) esta
condição for verdadeira, execute o código que está endetado”. Em Python,
uma instrução `if` é constituída das seguintes partes:

### Testescondicionais
Em cada instrução if está uma expressão que pode ser
avaliada como VERDADEIRA(True) ou FALSA(False), chamado de teste condicional. 
Python usa os valores `True` e `False` para decidir se o código em uma instrução `if` deve
ser executado. Se a condição tiver o valor como VERDADEIRO(True), Python
executará o código após a instrução `if`. Se o teste for avaliado como
FALSO(False), o Codigo depois da instrução if, será ignorado.


#escrever sobre expressões logicas
and, or, in etc....



### Instruçõesif
Ao entendermos os testes condicionais, fica facil entendermos como funciona as instruções `if`. 
Há vários tipos de instruções `if`, e a escolha de
qual deles usar dependerá do número de condições que devem ser
testadas.

#### if simples
A mais simples instrução if tem um teste e uma ação: 
`if teste_condicional: faça algo` 
Podemos colocar qualquer teste, condicional na primeira linha, e praticamente qualquer ação 
após o teste. Se o teste condicional for avaliado como VERDADEIRO `True`,
Python executará o código após a instrução `if`. Se o teste for avaliado
como FALSO `False`, Python ignorará o código depois da instrução `if`.


Temos uma variável que represent a idade de uma pessoa e queremos saber se essa pessoa 
tem idade suficiente para beber.
```
# definimos a idade 
idade = 19
# verifica se a condição é verdadeira se for ele executa o codigo
if idade >= 18:
    print("Opa, você pode beber, vamos tomar uma") 
```

