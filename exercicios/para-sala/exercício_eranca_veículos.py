

class Veiculo:
    def __init__(self,marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    def descricao(self):  
       return f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}'
   
   

class  Carro (Veiculo):
    def __init__(self, marca,modelo,ano, num_portas, cavalos):
                 #cavalos ):
        super().__init__ (marca,modelo,ano)  
        self.num_portas = num_portas
        self.cavalos = cavalos
    def descricao(self):  
       return super().descricao() + f'Portas: {self.num_portas}, Cavalos: { self.cavalos}'

class Moto(Veiculo):  
    def __init__(self, marca,modelo,ano, estilo, motor):
                 #motor ):
        super().__init__ (marca,modelo,ano)  
        self.estilo = estilo
        self.motor = motor
    def descricao(self):  
       return super().descricao() + f' Estilo: {self.estilo}, Motor: {self.motor}'
   #f'Estilo:{self.estilo}, Motor{self.motor}' + super().descricao      
    

carro = Carro( 'Toyota', 'Corolla', 2023, 4, 40)    
print (carro.descricao())
moto = Moto( 'Honda', 'ADV', 2023, 'street', 260)
print (moto.descricao())

carro_carol = Carro('Fiat', ' uno', 2023, 2 , 20) 
print (carro_carol.descricao())
moto_carol = Moto('Honda', ' PCX', 2018, ' Street', 150) 
print (moto_carol.descricao())

    
    
    
      