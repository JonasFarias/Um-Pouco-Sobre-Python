# IF(SE)


O tipo mais comum de instrução de controle de fluxo é a instrução `if`.
Uma instrução `if` pode ser lida como “se (if) esta
condição for verdadeira, execute o código que está endetado”. Em Python,
uma instrução `if` é constituída das seguintes partes:

### Testes condicionais

Em cada instrução if está uma expressão que pode ser
avaliada como VERDADEIRA(True) ou FALSA(False), chamado de teste condicional. 
Python usa os valores `True` e `False` para decidir se o código em uma instrução `if` deve
ser executado. Se a condição tiver o valor como VERDADEIRO(True), Python
executará o código após a instrução `if`. Se o teste for avaliado como
FALSO(False), o Codigo depois da instrução if, será ignorado.

### Verificando a igualdade `==`
Testes condicionais compara o valor atual de uma variável
com um valor específico de interesse. O teste condicional mais simples
verifica se o valor de uma variável é igual ao valor de interesse:
`
# Aqui definimos o valor da variavel doce sendo 'brigadeiro'
doce = 'brigadeiro'
# Aqui perguntamos se o valor de doce é igual a 'brigadeiro
doce == 'brigadeiro'
True
`

o sinal de `=' na linguaem python significa atribuição, então 
sempre que vermos um sinal de "=" no pyhton estamos atribuindo um valor
a uma varivael.
agora quando vemos dois sinais de igual "==", significa sinal de igualdade, 
então sempre que se vê `==` será sempre perguntando se o valor da viarivel é igual ao valor digitado.

Quando o valor de doce for diferente de 'brigadeiro', o valor do teste será False:

`
doce = 'brigadeiro'
doce == 'sorvete' 
False
`
Um único sinal de igual, na verdade, é uma instrução; você poderia ler o
código como “defina o valor de doce como 'brigadeiro'”. 
Por outro lado, um
sinal de igualdade duplo, faz uma pergunta: 
“O valor de doce é igual a 'sorvete'?”. 


### Verificando a diferença `!=`

