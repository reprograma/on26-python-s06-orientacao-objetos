class dog():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def to_walk(self):
        print('Im walking')
    def inf(self):
        print(self.name, self.breed)

dog_Frida= dog('Frida', 'Poolde')
dog_Batata_Doce= dog('Batata Doce', 'Poodle')
dog_Pipoca_Doce= dog('Pipoca doce', 'Pitbull toy')


dog_Frida.inf()
dog_Batata_Doce.to_walk()
dog_Pipoca_Doce.inf()

a=2
b=1
sol=b.__and__(a)
print(sol)