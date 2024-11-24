class animal: # generate the class 
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_age(self):
        return f"{self.name} is {self.age} years old"
    
class Dog(animal): # inherting the animal class 
    #class atrribute (shared by all instance )
    species = "cnies familiars"

   
    # instance method
    def bark(self):
        return f"{self.name} say woof"

    
class cat(animal):
    
    species = "cnies familiars"

    
    def meu(self):
        return f"{self.name} say meu"

   

 
cat1 =cat("cats",3)

dog1 = Dog("asdf",2)
dog2 = Dog("asdsdfsf",3)
print(dog1.bark())
print(dog2.get_age())
print(dog1.species)