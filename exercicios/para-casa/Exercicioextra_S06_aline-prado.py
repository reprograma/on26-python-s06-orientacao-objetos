"""Resolucão Exercício Extra"""

class Funcionario:
    def __init__(self, nome):
        self.nome = nome
        self.salario = 0.0  # salário inicial 0

    def calcular_pagamento(self):
        pass

class FuncionarioTemporario(Funcionario):
    def __init__(self, nome, salario_por_hora, horas_trabalhadas):
        super().__init__(nome)
        self.salario_por_hora = salario_por_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calcular_pagamento(self):
        return self.salario_por_hora * self.horas_trabalhadas

class FuncionarioIntegral(Funcionario):
    def __init__(self, nome, salario_mensal):
        super().__init__(nome)
        self.salario_mensal = salario_mensal

    def calcular_pagamento(self):
        return self.salario_mensal

# Instância Funcionário Temporário
funcionario_temporario = FuncionarioTemporario("João Silva", 15.0, 20)

# Instância Funcionário Integral
funcionario_integral = FuncionarioIntegral("Pedro Matos", 2500.00)

print(f"Pagamento do {funcionario_temporario.nome} é de R${funcionario_temporario.calcular_pagamento():.2f}")
print(f"Pagamento da {funcionario_integral.nome} é de R${funcionario_integral.calcular_pagamento():.2f}")
