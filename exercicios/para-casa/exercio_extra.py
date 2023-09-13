class Funcionario:
    def __init__(self, nome, salario):
        self.nome = str(nome)
        self.salario - 0

    def calcularPagamento(self):   
        pass

class Temporario(Funcionario):        
     def __init__(self, nome, salarioporhora, hora):
         self.nome = str(nome)
         self.salarioporhora = salarioporhora
         self.hora = hora

     def calcularPagamento(self):
         salario = self.salarioporhora * self.hora
         return salario

class FuncionarioIntegral(Funcionario):      #funcionario dentro do () para poder chamar a classe lá de cima       
    def __init__(self, nome, salariomensal):
        super().__init__(nome)
        self.salariomensal = salariomensal
   
    def calcularPagamento(self):
        return self.salariomensal
    
maria_funcionario = FuncionarioIntegral("Maria", 20.000)
andreza_funcionario = Temporario ("Andreza", 1500, 10)

print(maria_funcionario.calcularPagamento())  
print(andreza_funcionario.calcularPagamento())    
       