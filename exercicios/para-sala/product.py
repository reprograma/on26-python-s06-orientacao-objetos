class Product:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        
class Vinil(Product):
    def __init__(self, name, value, weight):
        super().__init__(name, value)
        self.name = name
        self.value = value
        self.weight = weight
    def info(self):
        print("Name ", self.name, "Value R$ ", self.value + "Weight ", self.weight)
        
class Digital(Product):
    def __init__(self, name, value, megabyte):
        super().__init__(name, value)
        self.name = name
        self.value = value
        self.megabyte = megabyte
    def info(self):
        print("Name ", self.name, "Value R$ ", self.value + "MegaByte", self.megabyte)
        
renaissancevinil = Vinil("Renaissance ", "400.00 ", " 20")
renaissancevinil.info()

renaissancedigital = Digital("Renaissance ", "150.00 ", "30 ")
renaissancedigital.info()