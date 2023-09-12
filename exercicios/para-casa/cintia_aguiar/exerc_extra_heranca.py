class Funcionario:
    def __init__(self, nome):
        self.nome = nome
        self.salario = 0.00

    def calcular_pagamento(self):
        return self.salario
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

temporario_1 = FuncionarioTemporario("Cintia Aguiar", 22.00, 95)
integral_1 = FuncionarioIntegral("Kenison Aguiar", 4800.00)

print(f"Funcionário Temporário 01 - Nome completo: {temporario_1.nome}, Salário ref. à AGO/2023: R${temporario_1.calcular_pagamento()}")
print(f"Funcionário Integral 01 - Nome completo: {integral_1.nome}, Salário ref. à AGO/2023: R${integral_1.calcular_pagamento()}")