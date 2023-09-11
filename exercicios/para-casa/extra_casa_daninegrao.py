'''Você está encarregado de criar um sistema de gerenciamento de funcionários para uma empresa. O sistema deve ser capaz de lidar com diferentes tipos de funcionários e calcular seus salários com base em suas características específicas. Para isso, você precisa implementar a hierarquia de classes apropriada usando herança em Python.

Instruções:

Crie uma classe base chamada Funcionario com os seguintes atributos:

 - nome: o nome do funcionário.
 - salario: o salário base do funcionário (inicialmente definido como 0).

A classe Funcionario deve ter um método chamado `calcular_pagamento()` que retorna o pagamento do funcionário. No entanto, este método deve ser definido como um método abstrato (utilizando `pass`) uma vez que cada tipo de funcionário (temporário e integral) calculará o pagamento de maneira diferente.

Crie uma classe chamada FuncionarioTemporario, que herda da classe Funcionario. Esta classe deve ter os seguintes atributos adicionais:

- salario_por_hora: o salário por hora do funcionário temporário.
- horas_trabalhadas: o número de horas trabalhadas pelo funcionário temporário.
Na classe FuncionarioTemporario, implemente o método `calcular_pagamento()` para calcular o pagamento do funcionário temporário com base no salário por hora e nas horas trabalhadas.

Crie uma classe chamada FuncionarioIntegral, que também herda da classe Funcionario. Esta classe deve ter um atributo adicional:

- salario_mensal: o salário mensal do funcionário integral.
Na classe FuncionarioIntegral, implemente o método `calcular_pagamento()` para calcular o pagamento do funcionário integral, que é igual ao seu salário mensal.

Crie instâncias de FuncionarioTemporario e FuncionarioIntegral, atribuindo valores adequados aos atributos de cada funcionário.

Calcule e imprima o pagamento de cada funcionário usando o método `calcular_pagamento()`.'''

class Funcionario:
    def __init__(self, nome):
        self.nome = nome
        self.salario = 0.0
    def calcular_pagamento(self):
        pass

class funcionario_temporario(Funcionario):
    def __init__(self, nome, salario_por_hora, horas_trabalhadas):
        super().__init__(nome)
        self.salario_por_hora = salario_por_hora
        self.horas_trabalhadas = horas_trabalhadas
    def calcular_pagamento(self):
        self.salario =+ self.salario_por_hora * self.horas_trabalhadas
        return f'Nome do funcionario: {self.nome}, Salário para funcionario temporario: R${self.salario}'

class funcionario_integral(Funcionario):
    def __init__(self, nome, salario_mensal):
        super().__init__(nome)
        self.salario_mensal = salario_mensal

    def calcular_pagamento(self):
        self.salario =+ self.salario_mensal
        return f'Nome do funcionario: {self.nome}, Salário integral: R${self.salario}'


colaborador_temporario = funcionario_temporario('Daniele Negrão', 33, 180)
print(colaborador_temporario.calcular_pagamento())

colaborador_integral = funcionario_integral('Gabriel Negrão', 1500)
print(colaborador_integral.calcular_pagamento())