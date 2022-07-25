# Zen de Python
Durante muito tempo, a linguagem de programação Perl foi o principal
sustentáculo da internet.
O lema da comunidade Perl na época era: “Há mais de uma
maneira de fazer algo”. As pessoas gostaram dessa postura por um tempo
porque a flexibilidade inscrita na linguagem possibilitava resolver a maior
parte dos problemas de várias maneiras. 
Essa abordagem era aceitável
enquanto trabalhávamos em nossos próprios projetos, mas, em algum
momento, as pessoas perceberam que a ênfase na flexibilidade dificultava a
manutenção de projetos grandes em longo prazo. Revisar código e tentar
descobrir o que outra pessoa pensou quando resolvia um problema
complexo era difícil, tedioso e consumia bastante tempo.
Programadores Python experientes incentivarão você a evitar a
complexidade e buscar a simplicidade sempre que for possível. A filosofia
da comunidade Python está contida no “Zen de Python” de Tim Peters.
Você pode acessar esse conjunto resumido de princípios para escrever um
bom código Python fornecendo import this ao seu interpretador. 
Elas vão ser importantes para você
como um programador Python iniciante.


```
PyDev console: starting.
Python 3.7.0b5 (v3.7.0b5:abb8802389, May 31 2018, 01:03:08) [MSC v.1913 32 bit (Intel)] on win32
import this
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```


Agora vamos entender esse tal Zen of Python
Beautiful is better than ugly
"Bonito é melhor que feio"

Se você desenvolve software, sabe que existem vários caminhos para chegar à solução. Em Python, quando isso acontece, escolhemos a "mais bonita", isto é: aquela que, visualmente, é mais elegante! Por exemplo, ao invés de fazer assim:
if funcao(x) && y == 0 || z == 'yes':
prefira:
if funcao(x) and y == 0 or z == 'yes':
Explicit is better than implicit
"Explícito é melhor que implícito"

Por ser uma linguagem bastante flexível, Python te possibilita solucionar um problema de diversas maneiras. De mesmo modo, também te possibilita "esconder" determinadas partes de código (para que o mesmo fique menor, por exemplo). Em Python nós preferimos a opção mais legível, ou seja, aquela que apresenta todos os elementos para se fazer entender (sem nada "escondido"). Por exemplo, use:
import os
print os.getcwd()
ao invés de:
from os import *
print getcwd()
Simple is better than complex
"Simples é melhor que complexo"

Esse ponto é uma junção dos últimos dois: seu código Python deve primar pela beleza e legibilidade, sem perder a simplicidade! Ou seja, ao desenvolver um código Python, não busque o caminho mais complexo! Tente manter simples! Por exemplo, se eu lhe pedir apenas para escrever tais dados em disco: dados = [{'peso': 10, 'cor': 'verde'}, {'peso': 15, 'cor': 'azul'}]. Alguém pode vir com tal solução:
import sqlalchemy
import sqlalchemy.types as sqltypes

def gravar(dados):
    db = sqlalchemy.create_engine('sqlite:///dados.db')
    db.echo = False
    metadata = sqlalchemy.MetaData(db)
        table = sqlalchemy.Table('dados', metadata,
        sqlalchemy.Column('id', sqltypes.Integer, primary_key=True),
        sqlalchemy.Column('peso', sqltypes.Float),
        sqlalchemy.Column('cor', sqltypes.String(32)),
    )
    table.create(checkfirst=True)

    for dado in dados:
        i = table.insert()
        i.execute(**dados)
E outro poderia vir com:
import json

def gravar(dados):
    with open('dados.json', 'w') as f:
        f.write(json.dumps(dados))
Dado o requisito de apenas gravar em disco, qual solução é mais simples?
Complex is better than complicated
"Complexo é melhor que complicado"

Quando a alternativa simples não é possível, fuja da solução complicada! Adote, primeiro, a solução complexa. Só use a solução "complicada" (código ilegível, de difícil manutenção e "difícil de explicar") quando realmente nenhuma das anteriores for possível!

Usando o mesmo requisito do Zen anterior ("gravar dados em disco"), mas agora sendo obrigatório o uso de um banco de dados. Alguém poderia vir com a mesma solução anterior (usando uma framework de Mapeamento Objeto Relacional - ORM - como o SQLAlchemy, por exemplo), assim como alguém poderia dar a seguinte solução:
import MySQLdb

def gravar(dados):
    db = MySQLdb.connect(user='usuario', passwd="senha", host='localhost', db="dados")

    c = db.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS dados
        id int(11) NOT NULL auto_increment,
        peso float,
        cor varchar(32)
        PRIMARY KEY id
        ENGINE=InnoDB CHARSET=utf8
    """)

    insert_sql = (
        "INSERT INTO dados (peso, cor) "
        "VALUES (%s, %s, %s)")

    for dado in dados:
        c.execute(insert_sql,
            (dado['peso'], dado['dor'])
        )
Essa solução é dita complicada pois é extremamente acoplada, dependente de implementação, pouco manutenível e exige conhecimento não apenas da linguagem em questão (Python, no caso) mas de SQL também!
Flat is better than nested
"Linear é melhor do que aninhado"

Evite criar estruturas dentro de estruturas que estão dentro de outra estrutura (dicts são estruturas poderosas, mas use-os com cuidado). Opte pela alternativa "linear", sem aninhá-las: isso resulta em um código mais legível e o acesso ao dado, mais simples. Faça:
if i > 0: 
    return funcao(i) 
elif i == 0: 
    return 0 
else: 
    return 2 * funcao(i)
ao invés de
if i>0: return funcao(i) 
elif i==0: return 0 
else: return 2 * funcao(i)
Sparse is better than dense
"Esparso é melhor que denso"

Em outras palavras: não tente "amontoar" muito código em uma linha. Lembre-se do primeiro tópico: "bonito é melhor que feio"!
Readability counts
"Legibilidade conta"

Esse tópico é bem simples: ao terminar de desenvolver, olhe seu código passando o olho rapidamente: você se sente bem ou te dá um calafrio? Se te dá calafrios, tente iterar sobre ele, dando "um tapa no visual"! Um exemplo simples (em Java):
public class ClassePrincipal {
    public static void main(String[] args) {
        System.out.println("Olá pythonistas!");
    }
}
e
print("Olá pythonistas!")
...
Special cases aren't special enough to break the rules. Although practicality beats purity
"Casos especiais não são especiais o bastante para quebrar as regras. Ainda que praticidade vença a pureza"

Nenhum caso é tão especial a ponto de passar por cima das regras! Lembre-se: nenhum! Ou seja, mesmo que a praticidade vença a pureza, mantenha-se atento às regras (e ao próprio Zen!).
Errors should never pass silently. Unless explicitly silenced
"Erros nunca devem passar silenciosamente. A menos que sejam explicitamente silenciados"

Nunca "silencie" uma exceção, a menos que a mesma seja explicitamente declarada e silenciada. Silenciar uma exceção é um erro grave de manutenção do código, pois pode esconder um erro, as vezes inofensivo, as vezes crítico! Portanto, tenha atenção! Não faça isso:
try:
    x = funcao(y)
except:
    pass
Faça, no mínimo:
try:
    x = funcao(y)
except:
    print("Deu ruim!")
In the face of ambiguity, refuse the temptation to guess
"Diante da ambiguidade, recuse a tentação de adivinhar"

Novamente, isso tem a ver com fazer seu código específico, limpo, bonito e está relacionado com o próximo Zen. Ao se deparar com um trecho de código que PODE dar errado SE tal, tal e tal condições sejam cumpridas tenha certeza de uma coisa: alguma hora essas condições VÃO se realizar e seu código VAI se comportar de maneira inesperada.
There should be one— and preferably only one —obvious way to do it. Although that way may not be obvious at first unless you’re Dutch
"Deveria haver um — e preferencialmente apenas um — modo óbvio para fazer algo. Embora esse modo possa não ser óbvio a princípio a menos que você seja holandês"

Diferente da forma como acontece em outras linguagens (Perl, por exemplo, defende exatamente o contrário), em Python se prega que deve existir apenas uma maneira de se chegar a uma solução do problema. Esse é um dos motivos que torna Python tão simples: não é difícil aprender uma linguagem quando se tem diversas maneiras de se fazer a mesma coisa?

A segunda parte faz referência ao criador do Python, Guido van Rossum - que é holandês. Por ser o criador da linguagem, faria sentido que aprender uma regra em Python seria mais fácil para ele do que qualquer outra pessoa, no geral.
Now is better than never. Although never is often better than right now
"Agora é melhor que nunca. Embora nunca freqüentemente seja melhor que já."

Não gaste tempo planejando demais e executando de menos! As vezes é melhor fazer uma primeira versão e iterar sobre ela até que a mesma esteja bonita, pythonicamente falando. Mas mesmo assim, não saia fazendo "qualquer coisas", apenas pelo fato de se ter algo: pense o mínimo na solução!
If the implementation is hard to explain, it’s a bad idea
"Se a implementação é difícil de explicar, é uma má idéia"

E novamente a simplicidade é pregada: se você ficou com dúvida sobre a sua própria implementação, revise-a!
If the implementation is easy to explain, it may be a good idea
"Se a implementação é fácil de explicar, pode ser uma boa ideia"

Agora, se a a solução é simples de ser explicada, ela pode (repita comigo: PODE) ser uma boa ideia. Mas não necessariamente saber explicar uma implementação precede uma boa implementação.
Namespaces are one honking great idea — let’s do more of those!
"Namespaces são uma grande ideia — vamos ter mais dessas!"

Namespaces são delimitadores abstratos que fornecem um contexto para aquilo que está sendo armazenado. No caso do Python, eles servem para dar mais simplicidade ao código e deixá-lo mais legível, ou seja, uma ótima ideia. Veja o exemplo a seguir:
import modelos.cachorro as cachorro
import modelos.gato as gato

def funcao():
    cachorro.perseguir(gato)
    
    
    
    fontes
    [*Python Academy*](https://pythonacademy.com.br/zen-of-python)
    livro curso intensivo de python uma introdução pratica
