# Exercício de Sala 🏫  

## Exercicío Classe, Atributo e Método

1) - Exercício de Classe, Atributo e Método (Nível Básico): Conta Bancária

Você está criando um programa para representar contas bancárias. Cada conta bancária tem um número de conta, um titular da conta e um saldo. Você precisa criar uma classe ContaBancaria para representar essas contas e fornecer métodos para realizar operações básicas, como depósito e saque.

`Instruções:`

Crie uma classe chamada ContaBancaria com os seguintes atributos:

numero_conta: o número da conta (um número inteiro).
titular_conta: o nome do titular da conta (uma string).
saldo: o saldo da conta (um número decimal, inicialmente definido como 0).
Implemente os seguintes métodos na classe ContaBancaria:

`__init__(self, numero_conta, titular_conta)`: O construtor que inicializa os atributos da conta.
depositar(self, valor): Um método que permite ao titular da conta depositar dinheiro na conta.
sacar(self, valor): Um método que permite ao titular da conta sacar dinheiro da conta, desde que haja saldo suficiente.

Exemplo:

```python
# Exemplo de uso:
conta = ContaBancaria(12345, "João da Silva")
print(f"Saldo inicial da conta de {conta.titular_conta}: R${conta.saldo}")

conta.depositar(1000)
print(f"Saldo após depósito: R${conta.saldo}")

conta.sacar(500)
print(f"Saldo após saque: R${conta.saldo}")
```


2) - Exercício de Classe, Atributo e Método (Nível Básico): Retângulo

Crie uma classe chamada Retangulo para representar retângulos. Cada retângulo tem largura e altura. A classe deve incluir métodos para calcular a área e o perímetro do retângulo.

Instruções:

Crie uma classe chamada Retangulo com os seguintes atributos:

largura: a largura do retângulo (um número decimal).
altura: a altura do retângulo (um número decimal).
Implemente os seguintes métodos na classe Retangulo:

__init__(self, largura, altura): O construtor que inicializa os atributos da largura e altura.
calcular_area(self): Um método que calcula a área do retângulo (área = largura * altura).
calcular_perimetro(self): Um método que calcula o perímetro do retângulo (perímetro = 2 * (largura + altura)).
Exemplo:

```python

# Exemplo de uso:
retangulo = Retangulo(5.0, 3.0)

area = retangulo.calcular_area()
perimetro = retangulo.calcular_perimetro()

print(f"Área do retângulo: {area}")
print(f"Perímetro do retângulo: {perimetro}")
```




## 2 - Exercicío Herança





---

Terminou o exercício? Dá uma olhada nessa checklist e confere se tá tudo certinho, combinado?!

- [ ] Fiz o fork do repositório.
- [ ] Clonei o fork na minha máquina (`git clone url-do-meu-fork`).
- [ ] Resolvi o exercício.
- [ ] Adicionei as mudanças. (`git add .` para adicionar todos os arquivos, ou `git add nome_do_arquivo` para adicionar um arquivo específico)
- [ ] Commitei a cada mudança significativa ou na finalização do exercício (`git commit -m "Mensagem do commit"`)
- [ ] Pushei os commits na minha branch (`git push origin nome-da-branch`)
