# class Animal:
#     def __init__(self, name):
#         self.name = name
        
#     def makes_sond(self):
#         pass
    
# class Dog(Animal):
#     def makes_sound(self):
#         return f"{self.name} Makes bark"
    
# class Cat(Animal):
#     def makes_sound(self):
#         return f"{self.name} Makes meow"
    

# dog_Beyoncé = Animal("Yummy")
# dog_Beyoncé = makes_sound("Bark Bark")

class Person:
    def __init__(self, nationality, gender, name, age):
        self.nationality = nationality
        self.gender = gender
        self.name = name
        self.age = age
    
    def info(self):
        print(self.nationality, self.gender, self.name, self.age)
        
class PersonProfessional(Person):
    def __init__(self, nationality, gender, name, age, sector, level):
        super().__init__(nationality, gender, name, age)
        self.setor = sector
        self.level = level
        
    def info(self):
        super().info()
        print("Sector", self.setor)
        print("Level", self.level)
        
Beyoncé_DB = PersonProfessional("American","Famele", "Beyoncé", "42", "Singer")
Beyoncé_DB.info()