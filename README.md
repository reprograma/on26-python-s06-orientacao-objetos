<h1 align="center">
  <img src="assets/reprograma-fundos-claros.png" alt="logo reprograma" width="500">
</h1>

# Tema da Aula

Turma Online on26 | Semana 6 | 2023 | Professora Daviny Letícia

### Instruções
Antes de começar, vamos organizar nosso setup.
* Fork esse repositório 
* Clone o fork na sua máquina (Para isso basta abrir o seu terminal e digitar `git clone url-do-seu-repositorio-forkado`)
* Entre na pasta do seu repositório (Para isso basta abrir o seu terminal e digitar `cd nome-do-seu-repositorio-forkado`)
* [Add outras intrucoes caso necessario]

### Conteúdo
O que veremos na aula de hoje?
* [O que é POO](#o-que-é-orientação-objetos)
* [Classe, Atributo e Metódo](#classe-atributo-e-metódo)
* [Herança](#herança)
* [Encapsulamento](#encapsulamento)

# O que é orientação objetos

Programação orientado objeto é uma forma de programar, foi proposto por Ole-Johan Dahl e Kristen Nygaard, do Centro de Computação Norueguês em Oslo. Conceitos da POO têm origem na Simula 67, uma linguagem desenhada para fazer simulações.

Um objeto é uma abstração de algum fato ou ente do mundo real, com atributos que representam as suas caraterísticas ou propriedades, e métodos que emulam o seu comportamento ou atividade. 

A POO divide em 4 pilares:
 - Abstração
 - Encapsulamento
 - Herança
 - Polimorfismo

A estrutura de POO começar com um `class`, `Variável de Class ou Variável de Instância` e `Método`

OBS.: Tudo no Python é Objeto.

Para provar:

```python 
a = 1
print(type(a))
```
saída: `<class 'int'>`

o objeto a foi criado pela class inteiro

com isto ele carega alguns métodos

```python
a = 1
res = a.__add__(2)
print(res)
```
A mesma coisa que

```python
a = 1
res = a + 2
print(res)
```
saída: `3`

#### o que é __ no inicio do método?

No mundo pythonico o __ e conhecido com underscore.


# Classe, Atributo e Metódo

Classe, atributo e método são conceitos fundamentais na programação orientada a objetos (POO). Vamos explicar cada um deles:

## Classe:

Uma classe é um modelo ou um plano para criar objetos. Ela define a estrutura e o comportamento dos objetos que serão criados com base nessa classe. Uma classe é como um "molde" que contém a descrição de como os objetos desse tipo devem ser criados e se comportar.

Por exemplo, se você estiver criando um sistema de gerenciamento de carros, poderá ter uma classe chamada Carro que define os atributos e métodos comuns a todos os carros, como modelo, ano, cor e métodos para ligar, desligar, acelerar, frear, etc.

## Atributo:

Um atributo é uma variável que pertence a uma classe e armazena informações sobre os objetos dessa classe. Os atributos representam as características dos objetos e definem seu estado. Em outras palavras, eles são as propriedades que um objeto da classe possui.

Usando o exemplo da classe Carro, os atributos podem ser modelo, ano, cor, etc. Cada objeto da classe Carro terá seus próprios valores para esses atributos.

Exemplo de definição de atributos em uma classe Python:

```python
class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo  # Atributo modelo
        self.ano = ano        # Atributo ano
        self.cor = cor        # Atributo cor
        ## Método:
```
Um método é uma função que pertence a uma classe e define o comportamento dos objetos dessa classe. Os métodos representam as ações que os objetos podem executar ou os cálculos que podem realizar.

Em nossa classe Carro, poderíamos ter métodos como ligar(), desligar(), acelerar(), frear(), que descrevem as ações que um carro pode realizar.

Exemplo de definição de métodos em uma classe Python:

```python
class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def ligar(self):
        print("O carro está ligado.")

    def desligar(self):
        print("O carro está desligado.")

    def acelerar(self):
        print("O carro está acelerando.")

    def frear(self):
        print("O carro está freando.")
```
Quando você cria objetos a partir de uma classe, esses objetos têm acesso aos atributos e métodos definidos na classe e podem utilizá-los para armazenar informações e realizar ações.

 # Herança
Herança é um dos princípios fundamentais da programação orientada a objetos (POO) e é uma maneira de criar uma nova classe, chamada classe derivada ou subclasse, a partir de uma classe existente, chamada classe base ou superclasse. A herança permite que a subclasse herde atributos e métodos da superclasse, promovendo a reutilização de código e facilitando a criação de hierarquias de classes.

Aqui estão os principais conceitos relacionados à herança:

 - `Superclasse (Classe Base):`

A superclasse é a classe existente da qual a nova classe é derivada.
Ela contém atributos e métodos que são compartilhados pelos objetos das subclasses.
Também é conhecida como classe base ou classe pai.

- `Subclasse (Classe Derivada):`

A subclasse é a nova classe criada com base na superclasse.
Ela herda todos os atributos e métodos da superclasse, podendo adicionar novos atributos e métodos ou substituir (sobrescrever) os métodos da superclasse, se necessário.
Também é conhecida como classe derivada ou classe filha.

 - `Herança de Atributos:`

A herança permite que os atributos definidos na superclasse sejam automaticamente disponíveis nas subclasses.
As subclasses podem adicionar atributos adicionais ou alterar os valores dos atributos herdados.
Herança de Métodos:

A herança permite que os métodos definidos na superclasse sejam automaticamente disponíveis nas subclasses.
As subclasses podem adicionar métodos adicionais ou substituir (sobrescrever) os métodos herdados para fornecer uma implementação específica.

Exemplo de Herança em Python:

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return f"{self.nome} faz um latido."

class Gato(Animal):
    def fazer_som(self):
        return f"{self.nome} faz um miado."
```

Neste exemplo, temos uma superclasse Animal com um atributo nome e um método fazer_som(). As subclasses Cachorro e Gato herdam de Animal e sobrescrevem o método fazer_som() para fornecer comportamentos específicos para cada tipo de animal.

Ao criar objetos a partir das subclasses, eles herdam automaticamente os atributos e métodos da superclasse, mas também podem ter seus próprios atributos e métodos exclusivos.

```python
rex = Cachorro("Rex")
whiskers = Gato("Whiskers")

print(rex.fazer_som())  # Saída: "Rex faz um latido."
print(whiskers.fazer_som())  # Saída: "Whiskers faz um miado."
```

Isso ilustra como a herança permite criar classes relacionadas hierarquicamente, compartilhando funcionalidades comuns e permitindo a extensão ou personalização em subclasses específicas.

 - `super()`

É uma função incorporada em Python que é usada para chamar métodos da classe base (superclasse) a partir de uma classe derivada (subclasse) quando você está fazendo herança. É comumente usado quando você deseja estender um método da superclasse na subclasse, mas ainda deseja executar o código da superclasse no método sobrescrito.

Aqui está um exemplo simples de como usar super() em Python:

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print("Som genérico de animal")

class Cachorro(Animal):
    def fazer_som(self):
        super().fazer_som()  # Chama o método fazer_som da superclasse Animal
        print("Latido")

rex = Cachorro("Rex")
rex.fazer_som()
```

# Encapsulamento

O encapsulamento é um dos quatro pilares da programação orientada a objetos (POO), sendo os outros três a herança, a abstração e o polimorfismo. O encapsulamento se concentra na ideia de "esconder" os detalhes internos de uma classe e fornecer uma interface controlada para interagir com os objetos dessa classe. Ele desempenha um papel fundamental na criação de código seguro, organizado e fácil de manter.

Aqui estão os principais conceitos relacionados ao encapsulamento:

 - `Acesso Controlado`: O encapsulamento permite controlar o acesso aos atributos e métodos de uma classe, especificando quais são públicos (acessíveis de fora da classe), protegidos (acessíveis apenas para subclasses) e privados (acessíveis apenas dentro da classe).

- `Atributos Privados`: Atributos privados são aqueles que são marcados com um prefixo de sublinhado duplo (__) antes do nome. Isso torna o atributo "privado" e indica que ele não deve ser acessado diretamente de fora da classe. No entanto, em Python, eles não são estritamente privados, mas são tratados como "name mangling" (ou seja, o nome real do atributo é alterado).

- `Métodos de Acesso (Getters e Setters)`: Para permitir a leitura e modificação de atributos privados, você pode fornecer métodos de acesso, geralmente chamados de "getters" para leitura e "setters" para modificação. Isso permite que você controle como os atributos privados são acessados e modificados.

 - `Encapsulamento em Python`: Em Python, não há restrições rígidas de acesso como em algumas outras linguagens de programação, como Java. No entanto, a convenção é usar um sublinhado simples (_) antes do nome de um atributo para indicar que ele deve ser tratado como "protegido" e não acessado diretamente de fora da classe. O uso de sublinhado duplo (__) indica atributos "privados".

Exemplo de Encapsulamento em Python:

```python

class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome  # Atributo privado
        self.__idade = idade  # Atributo privado

    # Método getter para o atributo nome
    def get_nome(self):
        return self.__nome

    # Método setter para o atributo nome
    def set_nome(self, novo_nome):
        if len(novo_nome) > 0:
            self.__nome = novo_nome

    # Método getter para o atributo idade
    def get_idade(self):
        return self.__idade

    # Método setter para o atributo idade
    def set_idade(self, nova_idade):
        if nova_idade >= 0:
            self.__idade = nova_idade

# Criando um objeto Pessoa
pessoa = Pessoa("João", 30)

# Usando os métodos getter e setter para acessar e modificar atributos privados
print(pessoa.get_nome())  # Saída: "João"
pessoa.set_idade(35)
print(pessoa.get_idade())  # Saída: 35
```

Neste exemplo, a classe Pessoa encapsula os atributos `__nome` e `__idade` como privados e fornece métodos de acesso (getters e setters) para esses atributos. Isso permite um controle mais preciso sobre como esses atributos podem ser lidos e modificados, tornando o código mais seguro e organizado.

***
### Exercícios 
* [Exercicio para sala](https://github.com/reprograma/on26-python-s06-orientacao-objetos/tree/main/exercicios/para-sala)
* [Exercicio para casa](https://github.com/reprograma/on26-python-s06-orientacao-objetos/tree/main/exercicios/para-casa)

### Material da aula 



### Links Úteis
- [PensePython2e](https://penseallen.github.io/PensePython2e/)
- [PyLadiesSP/Cursos](https://github.com/PyLadiesSP/Cursos)



<p align="center">
Desenvolvido com :purple_heart:  
</p>

