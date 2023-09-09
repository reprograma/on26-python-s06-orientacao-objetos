#forma para o objeto
class Cachorro: #classe que irá criar o objeto
        #__init__ = método construtor
                #self = aqui dentro
    def __init__(self, nome, raca):
        self.nome = nome #o nome tem que ser guardado dentro do atributo self.nome
        self.raca = raca

        #cada def <alguma coisa> é um método
    def andar(self):
        print("Estou andando")
    
    def info(self):
        print(self.nome, self.raca)

#nome do objeto
cachorro_lulu = Cachorro("lulu", "harrier")
                            #Atributos de nome e raça seguindo a ordem ali de cima. 
cachorro_rex = Cachorro("rex", "pincher")


# .info e .andar são chamados de métodos, que nós criamos
cachorro_lulu.info() #esse .info ele retorna oque está dentro do parenteses dos seus respectivos obejtos. (nesse caso aqui é lulu e harrier)

cachorro_rex.info()

cachorro_lulu.andar()#nesse caso o .andar vai imprimir o o print que foi colocado lá em cima.

cachorro_rex.andar()


a = 1
b = 2

resp = b.__add__(a) 
print(resp)