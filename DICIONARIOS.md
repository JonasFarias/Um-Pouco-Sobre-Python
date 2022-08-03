

# DICIONARIOS

### COMO DECLARAR UM DICIONARIO

Os dicionarios é representado entre chaves `{}`

```
carro = {'cor': 'preto', 'portas': 4}
print(carro['cor'])
print(carro['portas'])

```
Um dicionário é uma coleção de pares chave-valor. 
Cada chave é conectada a um valor, e você pode usar uma chave para acessar o valor
associado a ela. O valor de uma chave pode ser um número, uma string,
uma lista ou até mesmo outro dicionário. De fato, podemos usar
qualquer objeto que possa ser criado em Python como valor de um
dicionário.

Toda chave é associada a seu valor por meio de dois-pontos,
e pares chave-valor individuais são separados por vírgulas.

Exemplo:

```
carro = {'cor':'preto'}
# a saida vai ser preto

```
### Acessando valores em um dicionário

Para obter o valor associado a uma chave, especifique o nome do
dicionário e coloque a chave entre colchetes, como vemos a seguir:

```
carro = {'cor': 'preto'}
print(alien_0['color']) 
```
Essa instrução devolve o valor associado à chave
'cor' do dicionário carro: preto 

Podemos ter um número ilimitado de pares chave-valor em um dicionário.
O dicionário carro original com dois pares chave-valor: 

`
carro = {'cor': 'preto', 'portas': 4}
`
Agora podemos acessar a cor e a quantidade de portas.
Se um comprador quiser escolher o carro pela cor ou pela quantidade de portas, podemos consultar 
os valores.

### Adicionando novos valores

Dicionários são estruturas dinâmicas, e você pode adicionar novos valores
a um dicionário a qualquer momento. 
Por exemplo:
```
carro['motor'] = 'v8'
carro['estilo'] = 'esportivo'

```

Python não se importa com a ordem em que armazenamos
cada par chave-valor; ele só se importa com a conexão entre cada chave
e seu valor.

### Começando um dicionário vazio

Às vezes, precisaremoscomeçar com um dicionário vazio e então acrescentar novos valores a ele. 
Para começar a preencher um dicionário vazio.
`
jogos = {}
`
Por exemplo, eis o modo de criar o dicionário jogos usando esta
abordagem: 

```

jogos = {}
jogos['tiro'] = 'country-strike'
jogos['aventura'] = 'dino crises'


```