class Vehicle:
    def __init__(self, hallmark, type, year):
        self.hallmark = hallmark
        self.type = type
        self.age = year
        
class Car(Vehicle):
    def __init__(self, hallmark, type, year, doors):
        super().__init__(hallmark, type, year)
        self.hallmark = hallmark
        self.type = type
        self.age = year
        self.doors = doors
    
    def info(self):
        print("Hallmark ", self.hallmark, "Type ", self.type, "Year ", self.age + "Doors", self.doors)
        
class Motorcycle(Vehicle):
    def __init__(self, hallmark, type, year, motor):
        super().__init__(hallmark, type, year)
        self.hallmark = hallmark
        self.type = type
        self.age = year
        self.motor = motor
        
    def info(self):
        print("Hallmark ", self.hallmark, "Type ", self.type, "Year ", self.age + "Motor", self.motor)
        
car = Car("BMW ", "M3   ", "2024  ", "4")
car.info()

motorcycle = Motorcycle("BMW ", "1250 ", "2024  ", "Two-cylinder ")
motorcycle.info()

    